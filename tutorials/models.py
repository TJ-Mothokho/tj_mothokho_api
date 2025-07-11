from django.db import models
from projects.models import Tag
import uuid

# Create your models here.

class Tutorial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Link to Tag model
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return self.title