import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza
from pizzas.models import Comments

from pizzas.forms import Comments

"""
pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, ' ', p.pizza_name)
toppings = p.topping_set.all()
for t in toppings:
    print(t.topping_name)
comments = p.comments_set.all()
for c in comments:
    print(c.text)
"""



for i in Comments.objects.filter(id=2):
    print(i)

