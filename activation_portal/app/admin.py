from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ActivationCode, Credentials

admin.site.unregister(Group)


class ActivationCodeInline(admin.StackedInline):
    model = ActivationCode

    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Credentials)
class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('cea_login', 'cima_login', 'has_activation_code')
    inlines = [ActivationCodeInline]
    search_fields = ('cea_login', 'cima_login')

    def has_activation_code(self, obj):
        return hasattr(obj, 'activationcode')

    has_activation_code.boolean = True
