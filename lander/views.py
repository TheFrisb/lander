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
        context["testimonials"] = Testimonial.objects.all().order_by("order")
        context["chosen_product"] = self.get_chosen_product(context["products"])
        context["is_checkout"] = False
        context["site_settings"] = SiteSettings.get_solo()
        return context

    def get_chosen_product(self, products):
        return products[0] if products else None


def ok_response(request):
    return JsonResponse({"status": "ok"})
