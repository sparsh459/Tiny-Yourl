from django.shortcuts import render, redirect
import uuid    # to generate a unique id
from urlshortner.models import url # to save teh data in database
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# this will create a new url , save it in database and then fetch it to show
def create(request):
    if request.method == "POST":
        urrl = request.POST['link']  # to get the link we submitted in the webapp
        uid = str(uuid.uuid4())[:5]  # teh unique id generated is very long so cutting it down to only 5 variables
        new_url = url(link=urrl,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

# after we get the unique id url from urls.py in urlshortner, we pass it to go functionas pk which is then going to search models and check if a link is assigned to them and thenwell redirect to that link
def go(request, pk):
    url_details = url.objects.get(uuid=pk)
    return redirect(url_details.link)

