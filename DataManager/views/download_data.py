from DataManager.models import Reviews


from django import shortcuts
from django.http import HttpResponseNotFound
from django.views.generic import View


import pandas as pd
from io import BytesIO
import json


class DownloadData(View):
    model = Reviews
    def get(self,request,slug,data_type):
        try:
            rw = self.model.objects.get(slug=slug)
            if data_type == 'json':
                data = []
                for comment in rw.get_comments():
                    value = {"comment": comment.comment, }
                    if comment.tag == None:
                        value["tag"] = None
                    else:
                        value["tag"] = comment.tag.name
                    data.append(json.dumps(value))
                response = shortcuts.HttpResponse(str(data), content_type='application/vnd.ms-json')
                response['Content-Disposition'] = f'attachment; filename="{slug}.json"'
                return response
            elif data_type == 'xlsx':
                with BytesIO() as b:
                    # Use the StringIO object as the filehandle.
                    writer = pd.ExcelWriter(b, engine='xlsxwriter')
                    df = pd.DataFrame({
                        'comments':[comment.comment for comment in rw.get_comments()],
                        'tag':[comment.tag for comment in rw.get_comments()]
                    })
                    df.to_excel(writer, sheet_name=slug)
                    writer.save()
                    # Set up the Http response.
                    filename = f'{slug}.xlsx'
                    response = shortcuts.HttpResponse(
                        b.getvalue(),
                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    )
                    response['Content-Disposition'] = 'attachment; filename=%s' % filename
                    return response
            else:
                raise shortcuts.Http404
        except:
            return HttpResponseNotFound('<h1>File not exist</h1>')



