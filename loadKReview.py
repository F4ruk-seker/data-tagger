from DataManager.models import Comment
from DataManager.models import Reviews
from DataManager.models import Tag

import json
#
table = Reviews.objects.create(
    name='Köfteci yusuf YALOVA',
    explanation='20.01.2023 - veriler doğrudan tek bir şubeden alındı veri kaynağı : https://www.google.com/maps/place/K%C3%B6fteci+Yusuf/@40.4229058,28.8603544,11z/data=!4m12!1m2!2m1!1sk%C3%B6fteci+yusuf!3m8!1s0x14ca5ba06ba716cd:0xd2955b80bb80466c!8m2!3d40.4229027!4d29.1652049!9m1!1b1!15sCg5rw7ZmdGVjaSB5dXN1ZiIDiAEBWhAiDmvDtmZ0ZWNpIHl1c3VmkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11bwnxzbpv'
)
reviews = open('real_office_new.json','r',encoding='utf-8')
reviews = json.load(reviews)

# repeating data
print(f'{"#"*25} - START - {"#"*25}')
counter = 0
remaining_count = len(reviews)
for _ in reviews:
    counter += 1

#     tag_name = _.get('result')
    comment = _.get('text')
    # rate = _.get('rate')
#
    if len(str(counter))==1:
        print(f'| 0000{counter}/{remaining_count} | @ {comment[:43]}')
    if len(str(counter))==2:
        print(f'| 00{counter}/{remaining_count} | @ {comment[:43]}')
    if len(str(counter))==3:
        print(f'| 0{counter}/{remaining_count} | @ {comment[:43]}')
    if len(str(counter))>=4:
        print(f'| {counter}/{remaining_count} | @ {comment[:43]}')
#     tag = Tag.objects.get(name=tag_name)
    table.comments.create(comment=comment)
#
# print(f'{"#"*25} - END - {"#"*25}')
