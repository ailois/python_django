from django.db import models

# Create your models here.
class usertype(models.Model):
    name = models.CharField(max_length=50)

class userInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    # 外键关联
    user_type = models.ForeignKey('usertype',on_delete=models.CASCADE)