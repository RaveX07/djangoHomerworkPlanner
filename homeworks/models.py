from django.db import models

# Create your models here.
class Homework(models.Model):

    schoolClasses = [
        ("deutsch", "DEUSCH"),
        ("mathe", "MATHE"),
        ("englisch", "ENGLISCH"),
        ("französisch", "FRANZÖSISCH"),
        ("chemie", "CHEMIE"),
        ("physik", "PHYSIK"),
        ("biologie", "BIOLOGIE"),
        ("informatik", "INFORMATIK"),
        ("geschichte", "GESCHICHTE"),
        ("musik", "MUSIK"),
        ("religion", "RELIGION"),
        ("kunst", "KUNST")
    ]

    task = models.CharField(max_length=50)
    deadline = models.DateField()
    schoolClass = models.CharField(max_length=12, choices=schoolClasses, default="deutsch")
    done = models.BooleanField(default=False, editable=False)
    username = models.UUIDField(editable=False)
