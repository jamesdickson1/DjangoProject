from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Pizza, Topping, Comments
from .forms import Comment
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}

    return render(request,'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    comments = pizza.comments_set.all().order_by('-date_added')
    picture = Pizza.picture
    context = {'pizza':pizza,'toppings':toppings,'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

def comments(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = Comment()
    else:
        form = Comment(data=request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.pizza = pizza
            comments.save()

            return HttpResponseRedirect(reverse('pizzas:pizza',args=[pizza_id]))

    comments = Comments.objects.all()
    context = {'pizza': pizza, 'form': form,'comments':comments}
    return render(request, 'pizzas/comments.html', context)



