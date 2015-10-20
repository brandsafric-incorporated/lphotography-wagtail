import struct
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from wagtail.wagtailimages.models import Image, AbstractImage, AbstractRendition
from PIL import Image as PILImage
from numpy import array, amin
from scipy.cluster.vq import kmeans2


class SmartImage(AbstractImage):
    dominant_foreground_color = models.CharField(max_length=6, blank=True)
    dominant_midground_color = models.CharField(max_length=6, blank=True)
    dominant_background_color = models.CharField(max_length=6, blank=True)

    admin_form_fields = Image.admin_form_fields + ('dominant_foreground_color', 'dominant_background_color', 'dominant_midground_color')

    def save(self, update_fields=None, *args, **kwargs):
        adding = self._state.adding
        super(AbstractImage, self).save(*args, **kwargs)
        if adding or (update_fields and 'image' in update_fields):
            img = PILImage.open(self.file.path)
            img_data = array(img.getdata()).astype(float)

            min_color_value = amin(img_data)

            centroids, _ = kmeans2(img_data, 3, iter=20)
            dominant_colors = sorted(centroids.astype(int).tolist())

            bg, mg, fg = [struct.pack('BBB', *rgb_value).encode('hex') for rgb_value in dominant_colors]

            self.dominant_foreground_color = fg
            self.dominant_midground_color = mg
            self.dominant_background_color = bg
            self.save()


class SmartImageRendition(AbstractRendition):
    image = models.ForeignKey(SmartImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )


# Delete the source image file when an image is deleted
@receiver(pre_delete, sender=SmartImage)
def image_delete(sender, instance, **kwargs):
    instance.file.delete(False)


# Delete the rendition image file when a rendition is deleted
@receiver(pre_delete, sender=SmartImageRendition)
def rendition_delete(sender, instance, **kwargs):
    instance.file.delete(False)
