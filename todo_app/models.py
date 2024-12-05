from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure tag names are unique

    def __str__(self):
        return self.name


from django.db import models

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # auto-generated timestamp
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

    def __str__(self):
        return self.title
