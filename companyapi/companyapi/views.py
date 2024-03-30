from django.http import HttpResponse
# from django.urls import HttpResponse

def home_page(request):
    print("home page requested")
    return HttpResponse("This is home page")