from django.db import models


class Item(models.Model):
    client_id = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'client_id: {self.client_id}, number: {self.number}'
