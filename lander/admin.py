from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from lander.models import Product, Testimonial, SiteSettings


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


admin.site.register(SiteSettings, SingletonModelAdmin)
