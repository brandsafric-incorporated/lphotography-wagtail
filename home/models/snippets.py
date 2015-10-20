from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel

@register_snippet
class UserBio(models.Model):
    avatar = models.ForeignKey('SmartImage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    name = models.CharField(max_length=200)
    bio = RichTextField()

    panels = [
        FieldPanel('avatar'),
        FieldPanel('name'),
        FieldPanel('bio'),
    ]

    def __unicode__(self):
        return self.name


@register_snippet
class IndividualPromoteHeader(models.Model):
    site_title = models.CharField(max_length=200)
    site_subtitle = models.CharField(max_length=200)
    user_bio = models.ForeignKey('UserBio', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('site_title'),
        FieldPanel('site_subtitle'),
        FieldPanel('user_bio'),
    ]

    def __unicode__(self):
        return self.site_title + ' - ' + unicode(self.user_bio)
