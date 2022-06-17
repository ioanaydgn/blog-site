from ast import keyword
from audioop import add
from importlib.resources import contents
from operator import truediv
from tabnanny import verbose
from time import timezone
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

class Post(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), null=True, blank=True, unique=True)
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
        if not self.slug:
            temp_slug = slugify(self.title)
            in_slug = temp_slug
            add_num = None
            while True:
                if add_num:
                    in_slug = temp.slug + str(add_num)
                try:
                    is_slug = self.__class__.objects.get(slug=in_slug)
                except Exception:
                    is_slug = None
                if not is_slug:
                    self.slug = in_slug
                    break
                elif is_slug and add_num:
                    add_num += 1
                else:
                    add_num = 1
                continue
        super().save(*args,**kwargs)