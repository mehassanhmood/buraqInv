from django.shortcuts import render
from typing import Annotated, Optional
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return HttpResponse("This works!")

def hello(request):
    content = HttpResponse("Hello from this endpoint!")
    return content
def request_details(request):

    response = HttpResponse()

    path = request.path
    scheme = request.scheme
    method = request.method
    meta = request.META
    path_info = request.path_info
    response.headers["Age"] = 20

    msg = f"""<br>
        <br>Path: {path}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>Meta: {response.headers}
        <br>Path_Info: {path_info}
        """

    return HttpResponse(msg, content_type="text/html", charset='utf-8')



def menuitems(request,dish:Optional[str] = None):
    items = {
        "pasta": "Fettuccini ",
        "pizza": "Watan Piiza ",
        "Cheese cake": "Cheese cake factory",
    }
    if dish:
        return HttpResponse(items[dish])
    else:
        return HttpResponse(items)