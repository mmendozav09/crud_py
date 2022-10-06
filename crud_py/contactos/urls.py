from urllib.parse import urlparse
from django.urls import path
from contactos import views as v

app_name = 'aplication'

urlpatterns = [
    path('inicio/' , v.inicio , name = 'inicio' ),
    path('detail_<int:id>/', v.detail, name='detail'),
    path('create/', v.create_contacto, name='create' ),
    path('update_<int:id>//', v.update_contacto, name='update'),
    path('delete_<int:id>//', v.delete_contacto, name='delete')
]

