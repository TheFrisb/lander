from django.http import JsonResponse
# import _ from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from lander.models import Product, SiteSettings

testimonials = [
    {
        "model": "lander.testimonial",
        "pk": 5,
        "fields": {
            "created_at": "2025-03-17T01:27:00.428Z",
            "updated_at": "2025-03-17T17:58:41.508Z",
            "name": "Nemanja",
            "product": 3,
            "content": _(
                "Ordered it for my brother and his wife for their anniversary and it was completed overnight 🙏! They loved it. Great idea for birthdays, anniversaries, etc.",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 6,
        "fields": {
            "created_at": "2025-03-17T01:27:00.431Z",
            "updated_at": "2025-03-17T17:57:46.129Z",
            "name": "Marko",
            "product": 3,
            "content": _(
                "Great video! Made my day. This is an amazing idea! I don't know how you guys came up with this, but keep up with the good work!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 7,
        "fields": {
            "created_at": "2025-03-17T01:27:00.432Z",
            "updated_at": "2025-03-17T17:56:55.039Z",
            "name": "Jacob",
            "product": 3,
            "content": _(
                "You guys made my sister's new car celebration so fun, bright and memorable! She loved it so much. Actually everybody loved it. Thank you for the amazing vibes, beautiful smiles and the kisses lol. Sending back a lot of joy and love to this awesome team ❤️. The order was made in the evening, and the video was ready in the morning. Many thanks :)",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 8,
        "fields": {
            "created_at": "2025-03-17T01:27:00.433Z",
            "updated_at": "2025-03-17T17:55:27.971Z",
            "name": "Janine",
            "product": 3,
            "content": _(
                "Got the video exceptionally fast with high quality of work. Mom loved it. Great idea, and very professional and funny!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 9,
        "fields": {
            "created_at": "2025-03-17T01:27:00.434Z",
            "updated_at": "2025-03-17T17:54:52.285Z",
            "name": "Alexander",
            "product": 3,
            "content": _(
                "Got mine in less than 22 hrs i love you guys!!! Will order more funny videos for our friends!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 10,
        "fields": {
            "created_at": "2025-03-17T01:27:00.435Z",
            "updated_at": "2025-03-17T17:54:31.520Z",
            "name": "Stefan",
            "product": 3,
            "content": _(
                "Perfect gift! Keep up with the good work guys!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 11,
        "fields": {
            "created_at": "2025-03-17T01:27:00.436Z",
            "updated_at": "2025-03-17T17:53:56.256Z",
            "name": "Maria",
            "product": 3,
            "content": _(
                "Love it, got my video after one day of ordering. Definitely will order again 😀",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 12,
        "fields": {
            "created_at": "2025-03-17T01:27:00.437Z",
            "updated_at": "2025-03-17T17:53:36.620Z",
            "name": "Ana",
            "product": 3,
            "content": _(
                "THANK YOU SO MUCH. I love my video- I can't wait to show it to my mum. These guys are so energetic and my video was made so quickly! AMAZING",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 13,
        "fields": {
            "created_at": "2025-03-17T01:27:00.438Z",
            "updated_at": "2025-03-17T17:53:13.641Z",
            "name": "Liam",
            "product": 3,
            "content": _(
                "Wow, amazed at the quality, such a wonderful present for someone's graduation, will definitely order again.",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 14,
        "fields": {
            "created_at": "2025-03-17T01:27:00.440Z",
            "updated_at": "2025-03-17T17:52:18.288Z",
            "name": "Nikola",
            "product": 3,
            "content": _(
                "Thank you guys, this is so-so good! Extraordinary performance and delivery from your side! Keep up the good work!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 15,
        "fields": {
            "created_at": "2025-03-17T01:27:00.441Z",
            "updated_at": "2025-03-17T17:51:27.684Z",
            "name": "Duke",
            "product": 3,
            "content": _(
                "Perfect !!! Great performance, super funny. Done super fast in 1 day,Thank you girls so much! My grandad loved it, he said it was very sweet and he was so happy!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 16,
        "fields": {
            "created_at": "2025-03-17T01:27:00.442Z",
            "updated_at": "2025-03-17T17:50:37.061Z",
            "name": "Ivana",
            "product": 3,
            "content": _(
                "They are amazing, my partner is watching the video from them everyday. Thank you",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 17,
        "fields": {
            "created_at": "2025-03-17T01:27:00.443Z",
            "updated_at": "2025-03-17T17:50:08.259Z",
            "name": "Maxim",
            "product": 3,
            "content": _(
                "Love the video! Super satisfied with the humor and the creativity of the video. I highly recommend them.",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 18,
        "fields": {
            "created_at": "2025-03-17T01:27:00.444Z",
            "updated_at": "2025-03-17T17:49:38.639Z",
            "name": "Stefani",
            "product": 3,
            "content": _(
                "Very professional and amazing! Thanks for the laugh and love guys! Keep spreading joy!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 19,
        "fields": {
            "created_at": "2025-03-17T01:27:00.445Z",
            "updated_at": "2025-03-17T17:48:47.664Z",
            "name": "Filip",
            "product": 3,
            "content": _(
                "I picked the love team, and it was very very lovely and fun. Delivery was less than 24 hours. I am fully satisfied with the result!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 20,
        "fields": {
            "created_at": "2025-03-17T01:27:00.447Z",
            "updated_at": "2025-03-17T01:27:00.447Z",
            "name": "Adrian",
            "product": 3,
            "content": _(
                "Amazing and very quickly sent out to me even without paying for the rush. Great quality. Very funny. Thanks so much :)",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 21,
        "fields": {
            "created_at": "2025-03-17T01:27:00.448Z",
            "updated_at": "2025-03-17T17:47:05.911Z",
            "name": "Alex",
            "product": 3,
            "content": _(
                "Order came a day after ordering, very happy with the result and my brother enjoyed it.",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 22,
        "fields": {
            "created_at": "2025-03-17T01:27:00.449Z",
            "updated_at": "2025-03-17T17:46:38.361Z",
            "name": "Joanna",
            "product": 3,
            "content": _(
                "This was so fun! We loved it. I wanna order a thousand more! Great idea and so much happiness!",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 23,
        "fields": {
            "created_at": "2025-03-17T01:27:00.450Z",
            "updated_at": "2025-03-17T01:27:00.450Z",
            "name": "Sasha",
            "product": 3,
            "content": _(
                "Thanks for the best birthday video. I feel so happy",
            ),
            "order": 0,
        },
    },
    {
        "model": "lander.testimonial",
        "pk": 24,
        "fields": {
            "created_at": "2025-03-17T01:27:00.451Z",
            "updated_at": "2025-03-17T17:45:43.981Z",
            "name": "Luka",
            "product": 3,
            "content": _(
                "I placed an order on the 15th of march and the very next day i got my video greeting. I'm very happy with the result. Thank you so much. All the best, Luka",
            ),
            "order": 0,
        },
    },
]

celebration_types = [
    {
        "model": "lander.celebrationtypes",
        "pk": 1,
        "fields": {
            "created_at": "2025-03-17T13:30:03.823Z",
            "updated_at": "2025-03-17T14:46:42.423Z",
            "name": _(
                "Birthday",
            ),
            "order": 1,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 3,
        "fields": {
            "created_at": "2025-03-17T14:47:18.856Z",
            "updated_at": "2025-03-17T14:47:18.856Z",
            "name": _(
                "Mother's Day",
            ),
            "order": 2,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 2,
        "fields": {
            "created_at": "2025-03-17T14:47:08.798Z",
            "updated_at": "2025-03-17T14:47:08.798Z",
            "name": _(
                "Graduation",
            ),
            "order": 3,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 4,
        "fields": {
            "created_at": "2025-03-17T14:47:23.636Z",
            "updated_at": "2025-03-17T14:47:23.636Z",
            "name": _(
                "Father's Day",
            ),
            "order": 4,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 5,
        "fields": {
            "created_at": "2025-03-17T14:47:27.170Z",
            "updated_at": "2025-03-17T14:47:27.170Z",
            "name": _(
                "New Car",
            ),
            "order": 5,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 6,
        "fields": {
            "created_at": "2025-03-17T14:47:35.822Z",
            "updated_at": "2025-03-17T14:47:35.822Z",
            "name": _(
                "Newborn Baby",
            ),
            "order": 6,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 7,
        "fields": {
            "created_at": "2025-03-17T14:47:53.184Z",
            "updated_at": "2025-03-17T14:47:53.184Z",
            "name": _(
                "New House",
            ),
            "order": 7,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 8,
        "fields": {
            "created_at": "2025-03-17T14:47:57.886Z",
            "updated_at": "2025-03-17T14:47:57.886Z",
            "name": _(
                "Christmas",
            ),
            "order": 8,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 9,
        "fields": {
            "created_at": "2025-03-17T14:48:00.924Z",
            "updated_at": "2025-03-17T14:48:00.924Z",
            "name": _(
                "Easter",
            ),
            "order": 9,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 10,
        "fields": {
            "created_at": "2025-03-17T14:48:32.299Z",
            "updated_at": "2025-03-17T14:48:32.299Z",
            "name": _(
                "Ramadan",
            ),
            "order": 10,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 11,
        "fields": {
            "created_at": "2025-03-17T15:00:34.502Z",
            "updated_at": "2025-03-17T15:00:34.502Z",
            "name": _(
                "Anniversary",
            ),
            "order": 11,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 12,
        "fields": {
            "created_at": "2025-03-17T15:00:41.390Z",
            "updated_at": "2025-03-17T15:00:41.390Z",
            "name": _(
                "Car License",
            ),
            "order": 12,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 13,
        "fields": {
            "created_at": "2025-03-17T15:01:01.782Z",
            "updated_at": "2025-03-17T15:01:01.782Z",
            "name": _(
                "Retirement",
            ),
            "order": 13,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 14,
        "fields": {
            "created_at": "2025-03-17T15:05:15.662Z",
            "updated_at": "2025-03-17T15:05:15.662Z",
            "name": _(
                "Work Promotion",
            ),
            "order": 14,
        },
    },
    {
        "model": "lander.celebrationtypes",
        "pk": 15,
        "fields": {
            "created_at": "2025-03-17T15:16:16.853Z",
            "updated_at": "2025-03-17T15:16:16.853Z",
            "name": _(
                "Your Choice",
            ),
            "order": 15,
        },
    },
]


# Create your views here.
class LanderView(TemplateView):
    template_name = "lander/product_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().order_by("order")
        context["celebration_types"] = self.get_celebration_types()
        chosen_product = self.get_chosen_product(context["products"])

        context["testimonials"] = self.get_testimonials()
        context["chosen_product"] = chosen_product
        context["is_checkout"] = False
        context["site_settings"] = SiteSettings.get_solo()
        context["starting_from_price"] = (
            Product.objects.all().order_by("discount_price").first().discount_price
        )
        context["discount_percentage"] = (
                100 - (chosen_product.discount_price / chosen_product.regular_price) * 100
        )

        return context

    def get_testimonials(self):
        return [testimonial["fields"] for testimonial in testimonials]

    def get_celebration_types(self):
        return [celebration_type["fields"] for celebration_type in celebration_types]

    def get_chosen_product(self, products):
        return products.first() if products else None


def ok_response(request):
    return JsonResponse({"status": "ok"})
