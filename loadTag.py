from DataManager.models import Tag

tag_data = [
	{"name":"YETKİNLİK"},
	{"name":"İÇTEN"},
	{"name":"SAYGIN"},
	{"name":"GÜÇLÜ"},
	{"name":"HEYCAN"},
	{"name":"OLUMSUZ"}
]

for tag in tag_data:
    Tag.objects.create(
        name=tag.get('name'),
        explanation='Açıklama yok'
    )
