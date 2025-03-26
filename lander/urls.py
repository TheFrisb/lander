from django.urls import path

from .views import LanderView, ok_response, ClickHandlerView

app_name = "lander"
urlpatterns = [
    path("", LanderView.as_view(), name="lander"),
    path("api/v1/click/", ClickHandlerView.as_view(), name="click_handler"),
    path("api/v1/payments/handler/", ok_response, name="ok_response"),
    path("api/v1/payments/success/", ok_response, name="ok_response"),
    path("api/v1/payments/failure/", ok_response, name="ok_response"),
    path("api/v1/payments/transaction/handler/", ok_response, name="ok_response"),
]
