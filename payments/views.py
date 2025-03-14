from django.views.generic import TemplateView


# Create your views here.
class CheckoutView(TemplateView):
    template_name = 'payments/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_checkout"] = True
        context["active_product_id"] = kwargs.get("product_id")
        return context
