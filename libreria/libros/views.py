from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Author
from .forms import AuthorForm
from.models import Book
from .forms import bookForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
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

#------------------------------------------------------------------
#Vista para listar libros
def listarLibros(request):
    lista1 = Book.objects.all()
    a1= "hola mundo"
    context = {'lista1':lista1,'a1':a1,}
    template = loader.get_template('libros/libros.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un libro
def detail_viewBook(request, id):
    context = {}

    context['object'] = Book.objects.get(id = id)

    return render(request,'libros/libro_detalle.html',context)

#vista para crear libros.
def create_libro(request):

    context = {}

    form = bookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('libros')
    
    context['form'] = form
    return render(request,'libros/create_libro.html', context)

#vista para actualizar libros
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_libro(request,id):

    context = {}

    obj = get_object_or_404(Book, id = id)

    #formulario que contendra la instancia
    form = bookForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('libros')
    
    context['form'] = form

    return render(request, "libros/update_viewLibro.html", context)


#Vista para eliminar un libro
def delete_viewBook(request, id):

    context = {}

    obj = get_object_or_404(Book, id = id)

    if request.method == "POST":
        obj.delete()
        return redirect('libros')
    
    return render(request, "libros/delete_libro.html", context)

