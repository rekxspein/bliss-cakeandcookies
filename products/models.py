from django.db import models

#ProductCategory Model


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = " Product Categories"
        
    @staticmethod
    def get_all_product_categories():
        return ProductCategory.objects.all()



# Product Model

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    offer_price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to ='images/', default=None, blank=False)
    stock = models.IntegerField(default=1)
    category = models.ForeignKey(ProductCategory, related_name = 'product' ,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        return Product.objects.filter(category=category_id)
