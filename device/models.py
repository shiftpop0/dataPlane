from django.db import models

class netInfoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    port_speed = models.IntegerField(default=0)
    link_speed = models.IntegerField(default=0)