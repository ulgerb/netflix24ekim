from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(("Video Başlık"), max_length=50)
    text = models.TextField(("Konu"))
    image = models.FileField(("Video"), upload_to='', max_length=100)
    date_now = models.DateTimeField(("Tarih"),  auto_now_add=False)

    def __str__(self):
        return self.title