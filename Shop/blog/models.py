from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.name


class product(models.Model):
    ProductName = models.CharField(max_length=200)
    ShortDescription = models.CharField(max_length=100)
    Description = models.TextField()
    Data = models.DateField()
    Image = models.ImageField(null=True, blank=True ,upload_to="images/")
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.ProductName
    

    #-------------------------------------------Article search log----------------------------
    
class ArticleSerachLog(models.Model):
    body =models.TextField(null=True)
        

