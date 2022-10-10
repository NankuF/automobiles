import random

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from mixer.backend.django import mixer

from automobiles.models import Order, Auto, Mark, Color


class Command(BaseCommand):
    help = "Fill the database with data"

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Order.objects.all().delete()
        Auto.objects.all().delete()
        Mark.objects.all().delete()
        Color.objects.all().delete()

        superuser = get_user_model().objects.create_superuser(username='admin', password='123')
        user = get_user_model().objects.create_user(username='user', password='123')

        colors = ['white', 'blue', 'black', 'orange']
        created_colors = mixer.cycle(4).blend(Color, color=mixer.sequence(*colors))

        marks = ['Audi', 'BMW', 'Bentley']
        models = mixer.cycle(3).blend(Mark, mark=mixer.sequence(*marks))
        audi, bmw, bentley = models
        audi_models = ['r8', 'a4']

        created_audi = mixer.cycle(2).blend(Auto, mark=audi, model=mixer.sequence(*audi_models))
        bmw_models = ['x5', 'x1']
        created_bmw = mixer.cycle(2).blend(Auto, mark=bmw, model=mixer.sequence(*bmw_models))
        bentley_models = ['Bentayga', 'Continental']
        created_bentley = mixer.cycle(2).blend(Auto, mark=bentley, model=mixer.sequence(*bentley_models))
        autos = [*created_audi, *created_bmw, *created_bentley]
        mixer.cycle(20).blend(Order,
                              color=mixer.sequence(*created_colors),
                              auto=mixer.sequence(*autos),
                              auto_count=mixer.sequence(*[random.randrange(1, 100) for _ in range(20)]))
