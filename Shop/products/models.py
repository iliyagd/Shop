from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.name  





class product(models.Model):
    ProductName = models.CharField(max_length=200)
    ShortDescription = models.CharField(max_length=100)
    Amount = models.IntegerField()
    Description = models.TextField()
    Data = models.DateField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        return self.ProductName  
          

# -----------------------------------Aritcle search log------------------------------------
class ArticleSerachLog(models.Model):
    body =models.TextField(null=True)

# ----------------------------------- CartItem -----------------------------------
class CartItem(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=0)
    Created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.Product.ProductName
    

    