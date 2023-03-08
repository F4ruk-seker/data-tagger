from DataManager.models import Comment
from DataManager.models import Reviews
from DataManager.models import Tag

import json
#
table = Reviews.objects.create(
    name='Yorumlar',
    explanation='fixing : utf-8-tr'
)
reviews = open('comments.json','r',encoding='utf-8')
reviews = json.load(reviews)

# repeating data
print(f'{"#"*25} - START - {"#"*25}')
counter = 0
remaining_count = len(reviews)
for _ in reviews:
    counter += 1

    tag_name = _.get('result')
    comment = _.get('comment')

    if len(str(counter))==1:
        print(f'| 0000{counter}/{remaining_count} | @ {comment[:43]}')
    if len(str(counter))==2:
        print(f'| 00{counter}/{remaining_count} | @ {comment[:43]}')
    if len(str(counter))==3:
        print(f'| 0{counter}/{remaining_count} | @ {comment[:43]}')
    if len(str(counter))>=4:
        print(f'| {counter}/{remaining_count} | @ {comment[:43]}')
    #
    tag = Tag.objects.get(name=tag_name)
    table.comments.create(comment=comment,tag=tag)

print(f'{"#"*25} - END - {"#"*25}')
