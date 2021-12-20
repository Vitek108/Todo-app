from django.contrib.auth.models import User
from django.db import models


class Todo (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    comment = models.TextField(blank=True, default='')
    create_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    added_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    NEW = 'NW'
    IN_PROGRESS = 'IP'
    COMPLETED = 'CM'
    CANCELED = 'CD'
    STATUS_CHOICES = [
        (NEW, 'Nový úkol'),
        (IN_PROGRESS, 'V řešení'),
        (COMPLETED, 'Hotový'),
        (CANCELED, 'Zrušený')
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, unique=False, default=NEW)

    def __str__(self):
        return self.name
