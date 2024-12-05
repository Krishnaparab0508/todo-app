from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure tag names are unique

    def __str__(self):
        return self.name


from django.core.exceptions import ValidationError
from django.utils import timezone

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("OPEN", "OPEN"),
            ("WORKING", "WORKING"),
            ("PENDING REVIEW", "PENDING REVIEW"),
            ("COMPLETED", "COMPLETED"),
            ("OVERDUE", "OVERDUE"),
            ("CANCELLED", "CANCELLED"),
        ],
        default="OPEN",
    )
    tags = models.ManyToManyField("Tag", blank=True)

    def clean(self):
        # Check that the due date is not earlier than the timestamp
        if self.due_date and self.due_date < self.timestamp.date():
            raise ValidationError({'due_date': 'Due date cannot be earlier than the timestamp.'})

    def save(self, *args, **kwargs):
        # Call full_clean before saving to trigger the validation
        self.full_clean()
        super().save(*args, **kwargs)


