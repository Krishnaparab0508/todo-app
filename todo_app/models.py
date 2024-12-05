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
        # Ensure the timestamp is set before performing the check
        if self.timestamp and self.due_date:
            if self.due_date < self.timestamp.date():
                raise ValidationError("Due Date cannot be earlier than the Timestamp.")
        super().clean()

    def save(self, *args, **kwargs):
        # Call full_clean before saving to trigger the validation
        self.full_clean()
        super().save(*args, **kwargs)


