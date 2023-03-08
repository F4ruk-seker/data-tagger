from django.db.models.signals import pre_delete
from django.dispatch import receiver
from DataManager.models import Reviews


@receiver(pre_delete, sender=Reviews)
def reviews_post_delete(sender, instance, **kwargs):
    reviews = Reviews.objects.get(id=instance.id)
    reviews.comments.all().delete()
