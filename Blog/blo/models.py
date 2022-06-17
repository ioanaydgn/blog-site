from ast import keyword
from importlib.resources import contents
from tabnanny import verbose
from time import timezone
from django.db import models
from django.utils.translation import gettext as _

class Post(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    draft = models.BooleanField(_("Is Draft"), default=True)
    thumb = models.ImageField(_("Thumbnail"))
    keywords = models.CharField(_("Keywords"), max_length=2048,null=True, blank=True)
    date = models.DateTimeField(_("Publish Date"), null=True, blank=True)
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.draft and not self.date:
            self.date = timezone.now()
        super().save(*args,**kwargs)