from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def admin_redirect(request):
    if request.user.is_superuser or request.user.groups.filter(name='TuGrupo').exists():
        return redirect('/admin/')
    else:
        # Redirigir a una página diferente si el usuario no tiene permisos de administrador
        return redirect('pagina_no_permisos')

# En tus URLs


from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    #path('transactions/', include('transactions.urls')),
]