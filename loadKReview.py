from DataManager.models import Comment
from DataManager.models import Reviews

import json

table = Reviews.objects.create(
    name='köfteci yusuf',
    explanation='Google maps dan alınan yorumlar'
)
tyt = open('review.json','r')
tytData = json.load(tyt)

# repeating data
print('START')
counter = 0
for _ in tytData:
    counter += 1
    print(counter)
    table.comments.create(comment=_.get('text'),rate=_.get('rate'))
print('END')
