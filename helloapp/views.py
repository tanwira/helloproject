from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Person

# Create your views here.
def hello(request):
    return HttpResponse("Hello world!")

def create(request):
    p = Person(name = "John")
    p.save()
    return HttpResponse("Created")

def filterPerson(request, name):
    try:
        p = Person.objects.filter(name__contains="Joh")
    except Exception:
        return HttpResponse("Not found")
    return render(request, "show.html", {"name": p.name, "id":p.id})

def getPerson(request, name):
    try:
        p = Person.objects.get(name=name)
    except Exception:
        return HttpResponse("Not found")
    return render(request, "show.html", {"name": p.name, "id":p.id})
    #return HttpResponse(p.id)

class EditNameView(View):
    def get(self, request, name):
        p = get_object_or_404(Person, name=name)
        return render(request, "edit.html", {"name": p.name})

    def post(self, request, name):
        p = get_object_or_404(Person, name=name)
        p.name = request.POST["name"]
        p.save()
        # Always redirect after a successful POST request
        return HttpResponseRedirect('/get/' + p.name)


def set_name(request):
    request.session["name"] = "Tanwir"
    return HttpResponse("Name is set.")

def get_name(request):
    return HttpResponse(request.session["name"])