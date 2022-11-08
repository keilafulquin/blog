from django import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from AppBlog.views import (
    articulos,
    search_publicacion_view, 
    ArticuloList,
    ArticuloDetail,
    ArticuloUpdate,
    ArticuloDelete,
    ArticuloCrear,
    MyLogin,
    MyLogout,
    register,
    editar_perfil,
    agregar_avatar
)



urlpatterns = [
    path('search-post/', search_publicacion_view, name='Busqueda'),
    path('', ArticuloList.as_view(), name = 'Lista'),
    path(r'^nuevoarticulo$', ArticuloCrear.as_view(), name = "Nuevo Articulo"),
    path(r'^detail/articulo/(?P<pk>\d+)^$', ArticuloDetail.as_view(), name="ArticuloDetail"),
    path(r'^editar/articulo/(?P<pk>\d+)^$', ArticuloUpdate.as_view(), name="ArticuloEdit"),
    path(r'^borrar/articulo/(?P<pk>\d+)^$', ArticuloDelete.as_view(), name="ArticuloDelete"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)