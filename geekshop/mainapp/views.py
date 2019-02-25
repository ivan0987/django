from django.shortcuts import render
import os

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html', context=os.path.join('mainapp', '1.json'))


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
