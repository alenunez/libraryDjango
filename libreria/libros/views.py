from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Author
from .forms import AuthorForm

# Create your views here.
def index(request):
    template = loader.get_template('libros/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

#Vista para listar autores
def listarAutores(request):
    lista = Author.objects.all()
    a = "hola mundo"
    context = {'lista':lista,'a':a,}
    template = loader.get_template('autores/autores.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def detail_view(request, id):
    context = {}

    context['object'] = Author.objects.get(id = id)

    return render(request,'autores/autor_detalle.html',context)

#vista para crear autores.
def create_autor(request):

    context = {}

    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context['form'] = form
    return render(request,'autores/create_autor.html', context)

#vista para actualizar autores
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_autor(request,id):

    context = {}

    obj = get_object_or_404(Author, id = id)

    #formulario que contendra la instancia
    form = AuthorForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context['form'] = form

    return render(request, "autores/update_view.html", context)


#Vista para eliminar un autor
def delete_view(request, id):

    context = {}

    obj = get_object_or_404(Author, id = id)

    if request.method == "POST":
        obj.delete()
        return redirect('autores')
    
    return render(request, "autores/delete_view.html", context)
