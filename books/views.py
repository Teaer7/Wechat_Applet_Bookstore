from django.shortcuts import render

# Create your views here.
def bookHome(request):
    return render(request, 'book_home.html')


def bookClassi(request):
    return render(request, 'book_classi.html')