from django.shortcuts import render

# Create your views here.
def orderIndex(request):
    return render(request, 'order_index.html')