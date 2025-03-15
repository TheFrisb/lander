from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from lander.models import Product, Testimonial, SiteSettings, CelebrationTypes


# Register your models here.
@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "regular_price", "discount_price", "order"]
    search_fields = ["name"]
    list_filter = ["regular_price", "discount_price"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Testimonial)
class TestimonialAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "product", "order"]
    search_fields = ["name"]
    list_filter = ["product"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["product"]


@admin.register(CelebrationTypes)
class CelebrationTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "order"]
    search_fields = ["name"]
    readonly_fields = ["created_at", "updated_at"]

    class Meta:
        verbose_name_plural = "Celebration Types"


admin.site.register(SiteSettings, SingletonModelAdmin)
