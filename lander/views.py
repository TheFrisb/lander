from django.views.generic import TemplateView

from lander.models import Product


# Create your views here.
class LanderView(TemplateView):
    template_name = "lander/product_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().order_by("order")
        context["chosen_product_id"] = self.get_chosen_product_id(context["products"])
        context["is_checkout"] = False
        return context

    def get_chosen_product_id(self, products):
        return products[0].id if products else 0
