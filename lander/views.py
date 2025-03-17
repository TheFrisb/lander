from django.http import JsonResponse
from django.views.generic import TemplateView

from lander.models import Product, Testimonial, CelebrationTypes, SiteSettings


# Create your views here.
class LanderView(TemplateView):
    template_name = "lander/product_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().order_by("order")
        context["celebration_types"] = CelebrationTypes.objects.all().order_by("order")
        chosen_product = self.get_chosen_product(context["products"])

        context["testimonials"] = Testimonial.objects.all().order_by("order")
        context["chosen_product"] = chosen_product
        context["is_checkout"] = False
        context["site_settings"] = SiteSettings.get_solo()
        context["starting_from_price"] = (
            Product.objects.all().order_by("discount_price").first().discount_price
        )
        context["discount_percentage"] = (
                100 - (chosen_product.discount_price / chosen_product.regular_price) * 100
        )
        return context

    def get_chosen_product(self, products):
        return products.first() if products else None


def ok_response(request):
    return JsonResponse({"status": "ok"})
