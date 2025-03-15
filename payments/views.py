from django.views.generic import TemplateView

from lander.models import SiteSettings, Product


# Create your views here.
class CheckoutView(TemplateView):
    template_name = "payments/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_checkout"] = True
        context["chosen_product"] = Product.objects.get(id=kwargs["product_id"])
        context["products"] = Product.objects.all().order_by("order")
        context["is_checkout"] = True
        context["site_settings"] = SiteSettings.get_solo()
        return context
