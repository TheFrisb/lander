from django.urls import path

from payments.views import CheckoutView, post_checkout_url

app_name = "payments"
urlpatterns = [
    path("checkout/<int:product_id>/", CheckoutView.as_view(), name="checkout"),
    path("api/v1/checkout/", post_checkout_url, name="post_checkout"),
]
