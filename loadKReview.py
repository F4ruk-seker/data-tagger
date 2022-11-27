from DataManager.models import Comment
from DataManager.models import Reviews

import json

table = Reviews.objects.create(
    name='Test köfteci yusuf',
    explanation='test'
)
tyt = open('review.json','r')
tytData = json.load(tyt)

# repeating data

for _ in tytData:
    table.comments.create(comment=_.get('text'),rate=_.get('rate'))
