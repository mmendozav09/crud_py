from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm

from .models import Contacto

def inicio(request):
    contactos = Contacto.objects.all()
    context ={
        'contactos' : contactos
    }
    return render(request, 'contactos/inicio.html', context)



def detail(request, id):
    detail_contacto = get_object_or_404(Contacto, pk=id)
    context ={
        'detail_contacto' : detail_contacto
    }
    return render(request, 'contactos/detail.html', context )


def create_contacto(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid() :
            contact_form.save()
            return redirect('aplication:inicio')
    else:
        contact_form = ContactForm()
    return render(request, 'contactos/create.html', {'contact_form' : contact_form})


def update_contacto(request, id):
    contacto = get_object_or_404(Contacto , id = id)
    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance = contacto)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('aplication:inicio')
    else:
        contact_form = ContactForm()
        return render(request, 'contactos/editar.html', {'contact_form' : contact_form})

        
def delete_contacto(request , id):
    contacto = get_object_or_404(Contacto , id = id)

    if contacto : 
        contacto.delete()
        return redirect('aplication:inicio')