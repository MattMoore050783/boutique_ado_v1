from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IfOWqFQkej05g5ieipHvcBE6zrFakpeJlsfdN1jOuurGQTSby605M0oF1YT906RzM4nPIKn1bCafZMZ2sI4A0n700DJfbywJw',
        'client_secret': 'sk_test_51IfOWqFQkej05g5irrxgxWf9T2lfvguB9Xr2dgqqwLxJLBSzfnz21z9a2fhugnF9lc8TwhTadv7GoB7gtDoOuq3a00vqW1X40n',
    }

    return render(request, template, context)