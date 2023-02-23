from DataManager.models import Comment
from DataManager.models import Reviews
from DataManager.models import Tag

import json

table = Reviews.objects.create(
    name='Yorumlar',
    explanation='yorumlar'
)
tyt = open('comments.json','r',encoding='utf-8')
tytData = json.load(tyt)

# repeating data
print('START')
counter = 0
for _ in tytData:
    counter += 1
    print(counter)

    tag_name = _.get('result')
    comment = _.get('comment')
    if tag_name == 'YETKÄ°NLÄ°K':
        tag_name = 'YETKİNLİK'
    if tag_name == 'HEYECAN':
        tag_name = 'HEYCAN'
    print(tag_name)
    tag = Tag.objects.get(name=tag_name)

    table.comments.create(comment=comment,tag=tag)

print('END')
