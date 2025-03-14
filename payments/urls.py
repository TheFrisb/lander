from django.urls import path

from payments.views import CheckoutView

app_name = "payments"
urlpatterns = [
    path("checkout/<int:product_id>/", CheckoutView.as_view(), name="checkout"),
]
