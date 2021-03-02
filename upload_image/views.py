from django.shortcuts import redirect, render
from upload_image.models import *
from django.contrib import messages
from os import remove
from django_uploadimage.settings import BASE_DIR
# Create your views here.

def renderIndex(request):
    if request.method=='POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        genero = request.POST['genero']
        imagen = request.FILES.get('imagen')
        if titulo and autor and genero and imagen:
            newBook=Books(titulo=titulo,autor=autor,genero=genero,image=imagen)
            newBook.save()
            messages.add_message(request,messages.SUCCESS,'Nuevo Libro Guardado correctamente')
        else:
            messages.add_message(request,messages.ERROR,'Complete todos los campos')
        return redirect('/index/')
    else:
        libros = Books.objects.all()
        return render(request,'index.html',{'libros':libros})

def deleteBook(request,id):
    libro = Books.objects.get(id=id)
    libroURL = libro.image.url.split('/')
    libroURL = '\\'.join(libroURL)
    remove(str(BASE_DIR) + libroURL)
    libro.delete()
    messages.add_message(request,messages.SUCCESS,'El libro se elimino correctamente')

    return redirect('/index/')
