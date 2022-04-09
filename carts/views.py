from django.shortcuts import render

# Create your views here.
def cartIndex(request):
    return render(request, 'cart_index.html')