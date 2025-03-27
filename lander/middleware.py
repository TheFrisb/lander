from uuid import uuid4

from django.conf import settings
from django.urls import resolve

from .models import Event


class PageViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.session_key = settings.REQUEST_SESSION_ID

    def __call__(self, request):
        if self.session_key not in request.session:
            request.session[self.session_key] = str(uuid4())

        session_id = request.session[self.session_key]

        if not request.user.is_authenticated:
            try:
                resolved = resolve(request.path_info)
                url_name = resolved.url_name
            except:
                url_name = None

            if url_name == "lander":
                Event.objects.create(
                    event_type=Event.EventType.PAGE_VIEW,
                    session_id=session_id,
                    page_type=Event.PageType.LANDER,
                )
            elif url_name == "checkout":
                Event.objects.create(
                    event_type=Event.EventType.PAGE_VIEW,
                    session_id=session_id,
                    page_type=Event.PageType.CHECKOUT,
                )

        response = self.get_response(request)
        return response
