from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.db.models import Count, Q
from solo.admin import SingletonModelAdmin

from lander.models import Product, SiteSettings, Event


# Register your models here.
@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "regular_price", "discount_price", "order"]
    search_fields = ["name"]
    list_filter = ["regular_price", "discount_price"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ("session_id", "event_type", "page_type", "click_type", "created_at")
    list_filter = ("event_type", "page_type", "click_type")
    search_fields = ("session_id",)
    change_list_template = "admin/event_change_list.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        queryset = response.context_data["cl"].queryset

        # PageView counts
        pageview_qs = queryset.filter(event_type="page_view")
        pageview_counts = pageview_qs.aggregate(
            total_lander=Count("id", filter=Q(page_type="lander")),
            unique_lander=Count(
                "session_id", distinct=True, filter=Q(page_type="lander")
            ),
            total_checkout=Count("id", filter=Q(page_type="checkout")),
            unique_checkout=Count(
                "session_id", distinct=True, filter=Q(page_type="checkout")
            ),
            total_combined=Count("id"),
            unique_combined=Count("session_id", distinct=True),
        )

        # Clicks counts
        clicks_qs = queryset.filter(event_type="click")
        clicks_counts = clicks_qs.aggregate(
            total_change_product=Count("id", filter=Q(click_type="change_product")),
            unique_change_product=Count(
                "session_id", distinct=True, filter=Q(click_type="change_product")
            ),
            total_video_slide=Count("id", filter=Q(click_type="video_slide")),
            unique_video_slide=Count(
                "session_id", distinct=True, filter=Q(click_type="video_slide")
            ),
            total_combined=Count("id"),
            unique_combined=Count("session_id", distinct=True),
        )

        extra_context = extra_context or {}
        extra_context["pageview_counts"] = pageview_counts
        extra_context["clicks_counts"] = clicks_counts
        extra_context["counts_label"] = (
            f"Statistics for {request.GET.get('created_at__year')}-{request.GET.get('created_at__month')}-{request.GET.get('created_at__day')}"
            if "created_at__day" in request.GET
            else "Statistics for All Dates"
        )
        extra_context["initiate_checkout_count_percentage"] = (
            pageview_counts["total_checkout"] / pageview_counts["total_lander"] * 100
            if pageview_counts["total_lander"] != 0
            else 0
        )
        extra_context["initiate_checkout_unique_count_percentage"] = (
            pageview_counts["unique_checkout"] / pageview_counts["unique_lander"] * 100
            if pageview_counts["unique_lander"] != 0
            else 0
        )

        response.context_data.update(extra_context)
        return response


admin.site.register(SiteSettings, SingletonModelAdmin)
