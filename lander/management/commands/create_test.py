from django.core.management.base import BaseCommand

from lander.models import Testimonial, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        names = [
            "Nemanja",
            "Marko",
            "Jovan",
            "Jelena",
            "Aleksandar",
            "Stefan",
            "Marija",
            "Ana",
            "Darko",
            "Nikola",
            "Dragan",
            "Ivana",
            "Miloš",
            "Stefani",
            "Filip",
            "Adrian",
            "Vladimir",
            "Joanna",
            "Sasha",
            "Luka",
            "Nina",
        ]

        contents = [
            "Ordered it for my brother and his wife for their anniversary and it was completed overnight 🙏! they loved it. great idea for birthdays, anniversaries, etc.",
            "Great video! Made my day. Received it in 7 hours after placing an order. Totally recommend it!",
            "You guys made my sister's new car celebration so fun, bright and memorable! She loved it so much. Actually everybody loved it. Thank you for the amazing vibes, beautiful smiles and the kisses lol. Sending back a lot of joy and love to this awesome team ❤️. The order was made in the evening, and the video was ready in the morning. Many thanks :)",
            "Got the video within 24 hours. Mom loved it. Great idea, and very professional and funny",
            "Got mine in less than 22 hrs i love you guys!!! Will order more funny videos for our friends!",
            "Perfect gift!",
            "Love it, got my video after one day of ordering. Definitely will order again 😀",
            "THANK YOU SO MUCH. I love my video- I can't wait to show it to my mum. These guys are so energetic and my video was made so quickly! AMAZING",
            "Wow, amazed at the quality, such a wonderful present for someones graduation, will definitely use again.",
            "Thank you guys, this is so-so good and i got the video in 12 hours. It is extra quick. Much appreciated.",
            "Perfect !!! Great performance, super funny. Done super fast in 1 day,"
            "Thank you girls so much! My grandad loved it, he said it was very sweet and he was so happy",
            "They are amazing, my partner is watching his video from them everyday. Thank you",
            "Love the video! Super satisfied with the humor and the creativity of the video. I highly recommend them.",
            "Quick turn around time! Like 24 hours after I ordered. Thanks for the laugh and love guys! Keep spreading joy!",
            "I picketed the love team, and it was very very lovely and fun. Delivery was less than 24 hours without me paying extra.",
            "Amazing and very quickly sent out to me even without paying for the rush. Great quality. Very funny. Thanks so much :)",
            "Order came a day after ordering, very happy with the result and my brother enjoyed it.",
            "This was so fun! We loved it. I wanna order a thousand more! Great idea and so much happiness",
            "Thanks for the best birthday video. I feel so happy",
            "I placed an order on the 15th of march and the very next day i got my video greeting. I'm very happy with the result. Thank you so much. All the best, Nina",
        ]

        product = Product.objects.first()
        for name, content in zip(names, contents):
            Testimonial.objects.create(name=name, content=content, product=product)
