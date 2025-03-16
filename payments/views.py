import hashlib
import json

from django.http import JsonResponse
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


def post_checkout_url(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)

        email = data.get("email")
        total_price = data.get("total_price")

        if not email or not total_price:
            return JsonResponse({"error": "Missing email or total_price"}, status=400)

        redirect_url = get_redirect_url(total_price, email)
        return JsonResponse({"redirect_url": redirect_url}, status=200)

    except Exception as e:

        return JsonResponse({"error": "Internal server error"}, status=500)


def get_redirect_url(price, email):
    ids = "1984"  # merchant id
    key_shop = "6f90376a224c51b2c9d2bd4c604a31b6"  # merchant secret
    summ = price
    us_id = "10000293"  # payment id
    user_code = email
    paysys = "VisaEUR_V3"

    # get md5 hash
    hashed_hash = hashlib.md5(
        f"{ids}:{summ}:{key_shop}:{paysys}:{us_id}".encode()
    ).hexdigest()

    print(f"Produced hash: {hashed_hash}")

    base_url = "https://kassify.com/sci/"
    produced_url = f"{base_url}?ids={ids}&summ={summ}&us_id={us_id}&user_code={user_code}&paysys={paysys}&s={hashed_hash}"

    print(f"Produced url: {produced_url}")

    return produced_url
