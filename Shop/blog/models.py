from django.db import models

class product(models.Model):
    ProductName = models.CharField(max_length=200)
    ShortDescription = models.CharField(max_length=100)
    Description = models.TextField()
    Data = models.DateField()

    def __str__(self):
        return self.ProductName
        