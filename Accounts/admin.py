from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Accounts.models import *

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Мои поля',
            {'fields':
                 (
                  'descriptions',
                  'photo',
                  'vk_url',
                  'hh_url',
                  'behance_url',
                  'spec')
             }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Поля',
            {'fields':
                 (
                  'descriptions',
                  'photo',
                  'vk_url',
                  'hh_url',
                  'behance_url',
                  'spec',
                  'slug')
             }
        )
    )


admin.site.register(Image)
admin.site.register(Specs)
admin.site.register(Follow)
admin.site.register(Vacancy)