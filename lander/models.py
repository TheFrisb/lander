from django.db import models
from solo.models import SingletonModel


# Create your models here.
class BaseInternalModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseInternalModel):
    name = models.CharField(max_length=255, verbose_name="Team name")
    emoji = models.CharField(max_length=255, verbose_name="Emoji", blank=True)
    video = models.FileField(upload_to="videos/", verbose_name="Video")
    video_thumbnail = models.ImageField(
        upload_to="images/", verbose_name="Video thumbnail"
    )
    regular_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Regular price"
    )
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Discount price"
    )
    order = models.PositiveIntegerField(verbose_name="Order", default=0)

    def __str__(self):
        return f"{self.name} (${self.regular_price})"

    class Meta:
        ordering = ["order"]


class Testimonial(BaseInternalModel):
    name = models.CharField(max_length=255, verbose_name="Name")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    content = models.TextField(verbose_name="Content")
    order = models.PositiveIntegerField(verbose_name="Order", default=0)

    @property
    def name_initial(self):
        """
        Get the first letter of the name
        :return: str
        """
        return self.name[0]

    class Meta:
        ordering = ["order"]


class SiteSettings(SingletonModel, BaseInternalModel):
    how_to_order_video = models.FileField(
        upload_to="videos/", verbose_name="How to order video"
    )
    telegram_link = models.URLField(verbose_name="Telegram link")

    def __str__(self):
        return "Site settings"

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"


class CelebrationTypes(BaseInternalModel):
    name = models.CharField(max_length=255, verbose_name="Name")
    order = models.PositiveIntegerField(verbose_name="Order", default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order"]
