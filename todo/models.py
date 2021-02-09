from django.db import models
from datetime import datetime
from user.models import Users
# Create your models here.
# django.utils.timezone.now
class Todo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    tasks = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    due_date = models.DateField(null = True)
    is_complete = models.BooleanField(default=False)
    complete_percentage = models.DecimalField(max_digits=5,default=0,decimal_places=2)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
