from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from .models import CustomUser, BankAccount, SpecialUserGroup

class CustomUserAdmin(UserAdmin):
    # Configuración del admin de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from .models import BankAccount

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'account_number', 'balance', 'created_at')

    def owner_name(self, obj):
        return obj.owner.get_full_name()  

    owner_name.short_description = 'Owner Name'  

    def account_number(self, obj):
        return obj.account_number

    def created_at(self, obj):
        return obj.created_at

admin.site.register(BankAccount, BankAccountAdmin)


class SpecialUserGroupAdmin(admin.ModelAdmin):
    # Configuración del admin para el grupo especial
    pass

admin.site.register(SpecialUserGroup, SpecialUserGroupAdmin)

# Configura los permisos del grupo especial
special_user_permissions = Permission.objects.filter(
    codename__in=['add_transaction', 'change_transaction', 'delete_transaction']
)

# Obtiene o crea el grupo especial de usuarios
special_user_group, created = SpecialUserGroup.objects.get_or_create(name='Special Users')

# Asigna los permisos al grupo especial
special_user_group.permissions.set(special_user_permissions)
