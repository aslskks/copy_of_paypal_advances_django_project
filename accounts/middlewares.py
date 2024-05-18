from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/adm/') and request.user.is_superuser:
            return redirect(reverse('admin:index'))  # Redirigir a la página de administrador de Django
        return self.get_response(request)
