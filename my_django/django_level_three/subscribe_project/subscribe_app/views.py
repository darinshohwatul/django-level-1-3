from django.shortcuts import render
from subscribe_app.models import Customer

# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers':customer_list}
    render render(request, 'subscribe_app/customers.html', context=customer_dict)