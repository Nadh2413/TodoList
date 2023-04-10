from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    # Khoa ngoai ket noi 2 model ( 2 table voi nhau)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=2000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name
    