from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from lander.models import Product, SiteSettings


# Register your models here.
@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "regular_price", "discount_price", "order"]
    search_fields = ["name"]
    list_filter = ["regular_price", "discount_price"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(SiteSettings, SingletonModelAdmin)
