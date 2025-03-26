import hashlib
import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from lander.models import SiteSettings, Product

logger = logging.getLogger(__name__)


# Create your views here.
class CheckoutView(TemplateView):
    template_name = "payments/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            product = Product.objects.get(id=kwargs["product_id"])
        except Product.DoesNotExist:
            logger.warning(f"Product with id {kwargs['product_id']} does not exist")
            product = Product.objects.all().order_by("order").first()

        context["is_checkout"] = True
        context["chosen_product"] = Product.objects.get(id=kwargs["product_id"])
        context["products"] = Product.objects.all().order_by("order")
        context["is_checkout"] = True
        context["site_settings"] = SiteSettings.get_solo()
        context["starting_from_price"] = (
            Product.objects.all().order_by("discount_price").first().discount_price
        )
        return context


def post_checkout_url(request):
    logger.info("Received POST request to /checkout_url")
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)

        email = data.get("email")
        total_price = data.get("total_price")

        if not email or not total_price:
            logger.warning(f"Missing email or total_price in request body: {data}")
            return JsonResponse({"error": "Missing email or total_price"}, status=400)

        redirect_url = get_redirect_url(total_price, email)
        return JsonResponse({"redirect_url": redirect_url}, status=200)

    except Exception as e:
        logger.error(f"Error occurred while processing payment POST request: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)


def get_redirect_url(price, email):
    ids = settings.MERCHANT_ID
    key_shop = settings.MERCHANT_SECRET
    summ = price
    us_id = "10000293"  # payment id
    user_code = email
    paysys = "VisaEUR_V3"

    # get md5 hash
    hashed_hash = hashlib.md5(
        f"{ids}:{summ}:{key_shop}:{paysys}:{us_id}".encode()
    ).hexdigest()

    base_url = settings.MERCHANT_BASE_URL
    produced_url = f"{base_url}?ids={ids}&summ={summ}&us_id={us_id}&user_code={user_code}&paysys={paysys}&s={hashed_hash}"

    return produced_url
