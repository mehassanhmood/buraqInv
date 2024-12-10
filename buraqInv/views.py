from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    return HttpResponse("Nope")

def home(request):
    return HttpResponse("Project Home Pgae")