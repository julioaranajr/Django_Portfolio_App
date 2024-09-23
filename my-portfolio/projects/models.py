from django.db import models
from PIL import Image


class Project(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(default="About This project.")
    description = models.TextField(default="Description of this project.")
    status = models.CharField(
        max_length=25,
        default="In Progress",
        choices=[
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
            ("Backstage", "Backstage"),
            ("Planning", "Planning"),
        ],
    )
    pub_date = models.DateTimeField("date published", null=True, blank=True)
    technology = models.CharField(
        max_length=255, default="Python, Django, HTML, CSS, JS"
    )
    image = models.FileField(upload_to="project_images/", blank=True)
    # slug = models.SlugField(max_length=100, unique=True, blank=True, default="")

    def __str__(self):
        return f"{self.title} - {self.pub_date}"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 512 or img.width > 512:
            output_size = (512, 512)
            img.thumbnail(output_size)
            img.save(self.image.path)
