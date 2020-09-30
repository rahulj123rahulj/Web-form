from django.db import models

class contact_us(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=200)
    email=models.EmailField()
    query=models.CharField(max_length=200)

    def __str__(self):
        return self.name