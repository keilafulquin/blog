from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import (  
    Articulo,
    Avatar,
    
    
)
from AppBlog.forms import (
    ArticuloForm,
    AvatarForm,
    UserEditionForm
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required        
def articulos(request):
    
    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppBlog/articulos.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ArticuloForm(request.POST, request.FILES )
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo=datos_ingresados_por_usuario["titulo"],
                subtitulo=datos_ingresados_por_usuario["subtitulo"],
                cuerpo=datos_ingresados_por_usuario["cuerpo"],
                autor=datos_ingresados_por_usuario["autor"],
                imagen = datos_ingresados_por_usuario["imagen"]
            )
            nuevo_modelo.save()

            return render(request, "Applog/inicio.html", )

        contexto = {"formulario": mi_formulario, 'message':'¡Publicación creada con exito!'}
        return render(request, "AppBlog/articulos.html", context=contexto)


@login_required
def search_publicacion_view(request):
  
    articulos = Articulo.objects.filter(titulo=request.GET['search'])
    
    if len(articulos) == 0:
        context = {'error_no_results':'No se encontraron posts con ese título.'}
        return render(request,'AppBlog/busqueda-articulo.html', context=context)

    elif articulos == 1:

        context = {'articulos': articulos}
        return render(request,'AppBlog/busqueda-articulo.html', context=context)

    else:
        context = {'articulos': articulos}
        return render(request,'AppBlog/articulo_list', context=context)

  
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)






class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = "AppBlog/articulo_list.html"


class ArticuloDetail(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = "AppBlog/articulo_detail.html"


class ArticuloCrear(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = "/AppBlog/"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']


class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = "/AppBlog/"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']


class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = "/AppBlog/"



from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class MyLogin(LoginView):
    template_name = "AppBlog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "AppBlog/logout.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(request, "AppBlog/login.html", {"mensaje": f"Bienvenido/a: {username_capturado}!"})

    else:
        form = UserCreationForm()

    return render(request, "AppBlog/register.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "AppBlog/articulo_list.html", {"avatar": avatar.imagen.url})

    contexto = {
        "user": user,
        "form": form,
        "avatar": avatar.imagen.url
    }
    return render(request, "AppBlog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "AppBlog/articulo_list.html")

    contexto = {"form": form}
    return render(request, "AppBlog/avatar_form.html", contexto)