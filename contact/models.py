from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
