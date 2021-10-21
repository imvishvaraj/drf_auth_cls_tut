from django.db import models
from django.contrib.auth.models import User
import uuid


class MyFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    file = models.FileField(blank=False, null=False, upload_to='files/%Y/%b/')
    description = models.CharField(max_length=255)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_by = models.EmailField(blank=False, null=False)
