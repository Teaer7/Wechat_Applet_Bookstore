from django.shortcuts import render

# Create your views here.
def userIndex(request):
    return render(request, 'user_index.html')