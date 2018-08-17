from django.db import models


class Command(models.Model):
    denon_code = models.CharField(max_length=10)
    readable_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    queryable = models.BooleanField(default=False)
    icon_code = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.denon_code} ({self.readable_name})'


class Parameter(models.Model):
    denon_code = models.CharField(max_length=25)
    readable_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    icon_code = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.denon_code} ({self.readable_name})'
