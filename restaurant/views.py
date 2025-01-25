from django.shortcuts import render
from .models import Product,Order
from .forms import OrderForm

def ShowProduct(request):

    products = Product.objects.all()
    context = {
        "products":products
    }
    print(products)
    return render(request, "products.html",context)


def CreateOrder(request):

    form = OrderForm(request.POST or None, request.FILES or None)
    first_line = "Your Last Order was : \n\n"
    content_to_show = ""
    if form.is_valid():
        content_to_show += f"Customer name : {form.cleaned_data['customer_name']}\n\n"
        order_total = 0
        for product in form.cleaned_data['product']:
            content_to_show += f"{product.name} : {product.price}\n"
            order_total += product.price
        content_to_show += f"\nOrder Total : Rs {order_total}"
        form.save()
    if content_to_show:
        content_to_show = first_line + content_to_show
    context = {
        "form":form,
        "content_to_show":content_to_show
    }

    return render(request, "order.html",context)
