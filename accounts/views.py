# En tu archivo views.py


from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def adm_dashboard(request):
    if request.user.is_staff:
        return redirect('admin:index')  # Si el usuario es un superusuario, redirige a la interfaz de administración estándar
    else:
        # Si el usuario es un usuario normal, renderiza una plantilla personalizada para la interfaz de administración de usuarios normales
        return render(request, 'accounts/adm_dashboard.html')



from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from .models import UserProfile, Transaction  # Importa tus modelos necesarios


@login_required
def user_dashboard(request):
    # Obtener el usuario actual
    user = request.user
    
    # Obtener el perfil del usuario (debes ajustar esto según tu modelo de datos)
    user_profile = UserProfile.objects.get(user=user)
    
    # Obtener las transacciones del usuario (por ejemplo)
    transactions = Transaction.objects.filter(user=user)
    
    # Pasar los datos al contexto de renderizado
    context = {
        'user_profile': user_profile,
        'transactions': transactions,
    }
    
    # Renderizar la plantilla del dashboard de usuario con el contexto
    return render(request, 'user_dashboard.html', context)

@staff_member_required
def admin_dashboard(request):
    # Obtener todos los perfiles de usuario (por ejemplo)
    user_profiles = UserProfile.objects.all()
    
    # Obtener todas las transacciones (por ejemplo)
    transactions = Transaction.objects.all()
    
    # Pasar los datos al contexto de renderizado
    context = {
        'user_profiles': user_profiles,
        'transactions': transactions,
    }
    
    # Renderizar la plantilla del dashboard de administrador con el contexto
    return render(request, 'admin_dashboard.html', context)


@login_required
def admin_redirect(request):
    if request.user.is_superuser or request.user.groups.filter(name='Admin Group').exists():  # Corrige la lógica de comprobación de permisos
        return redirect('admin_dashboard')  # Redirige a la vista del dashboard del administrador
    else:
        return redirect('user_dashboard') 

from transactions.forms import TransferForm
from accounts.models import UserProfile  # Corrige la importación aquí
from .models import Transaction

# accounts/views.py

# accounts/views.py

from django.shortcuts import render, redirect
from transactions.forms import TransferForm
from django.contrib.auth.decorators import login_required

@login_required
def transfer_view(request):
    if request.method == 'POST':
        form = TransferForm(user=request.user.userprofile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Cambia 'success_url' por la URL de destino después de un éxito
    else:
        form = TransferForm(user=request.user.userprofile)
    
    return render(request, 'transfer.html', {'form': form})
