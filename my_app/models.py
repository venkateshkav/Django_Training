from django.db import models

# Create your models here.
#orm query 

class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    mail = models.EmailField(unique=True)
    course=models.CharField()
    dob=models.DateField()
    mobile = models.CharField(max_length=12)
    address= models.CharField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}-{self.age}--{self.mail}--{self.course}--{self.dob}--{self.mobile}--{self.address}"


class Category(models.Model):
    name= models.CharField(max_length=45)
    des = models.CharField(max_length=67,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
    


class Products(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    #CASCADE => if category deleted, products also get deleted
    #SET_DEFAULT => it will set the given default vaulue
    #SET_NULL => it will assign null as value
    #PROTECT => it will raise an error
    #Do_Nothing: it wont do anything

    def __str__(self):
        return f"{self.name}-{self.stock}"  
class ImageModel(models.Model):
    image = models.ImageField(upload_to='pictures' )
    created_at = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.image



