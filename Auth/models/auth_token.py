from django.db import models
import uuid


class AuthToken(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('Account.CustomUserModel', on_delete=models.CASCADE, blank=True, null=True)
    life = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.token} |-> {self.user}'
