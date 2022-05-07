from django.contrib import admin

# Register your models here.

from .models import Pizza
from .models import Topping
from .models import Comments

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comments)
