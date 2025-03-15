import hashlib

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

        self.log_hash()
        return context

    def log_hash(self):
        ids = "1984"  # merchant id
        key_shop = "6f90376a224c51b2c9d2bd4c604a31b6"  # merchant secret
        summ = "59.99"  # sum to pay
        us_id = "10000293"  # payment id
        user_code = "1"
        paysys = "Tether"

        # get md5 hash
        hashed_hash = hashlib.md5(
            f"{ids}:{summ}:{key_shop}:{paysys}:{us_id}".encode()
        ).hexdigest()

        print(f"Produced hash: {hashed_hash}")

        base_url = "https://kassify.com/sci/"
        produced_url = f"{base_url}?ids={ids}&summ={summ}&us_id={us_id}&user_code={user_code}&paysys={paysys}&s={hashed_hash}"

        print(f"Produced url: {produced_url}")

    def get_chosen_product(self, products):
        return products[0] if products else None


def ok_response(request):
    return JsonResponse({"status": "ok"})
