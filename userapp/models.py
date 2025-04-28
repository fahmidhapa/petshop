from django.db import models

# Create your models here.
# class classname inheritence

class Reg_tbl(models.Model):
    fnm = models.CharField(max_length=30)
    eml = models.EmailField()
    mob = models.IntegerField()
    psw = models.CharField(max_length=20)
    cpsw = models.CharField(max_length=20)


class pet_tbl(models.Model):
    pnm=models.CharField(max_length=30)
    prc =models.IntegerField()
    pim=models.FileField(upload_to='pic')
    des=models.TextField()

class cart_tbl(models.Model):
    user = models.ForeignKey(Reg_tbl,on_delete=models.CASCADE)
    pet = models.ForeignKey(pet_tbl,on_delete=models.CASCADE)
    qty =models.PositiveIntegerField(default=1)
    