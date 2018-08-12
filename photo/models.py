from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Image(models.Model):
    user = models.ForeignKey(User, related_name='photo', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    slug = models.SlugField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    photo = models.ImageField(upload_to='images/%Y%m%d')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Image)
def del_image(sender, instance, **kwargs):
    instance.image.delete(False)
