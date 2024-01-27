from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)

    # Recommend to use for every model, because it's very important while storing the big data in database.
    # Can see when data was created and modified previously
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Set a string representation of this model
    def __str__(self):
        return self.task