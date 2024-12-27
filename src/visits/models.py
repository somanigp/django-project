from django.db import models

# Create your models here. For ORM mapping.
class PageVisit(models.Model):
    # This maps to a db table, Object-Relational Mapper.
    # invisible col -> id -> primary key -> autofield -> 1, 2, 3..
    # ** https://docs.djangoproject.com/en/5.1/topics/db/models/#fields
    path = models.TextField(blank=True, null=True)  # path is a Column
    # * Everytime create is called for this class, that time value is put in below field.
    timestamp = models.DateTimeField(auto_now_add=True) # timestamp is a Column
    
