from django.contrib import admin
from RPJOGA.models import char

# Register your models here.


class charAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hp', 'estamina')
    list_filter = ('nome',)

admin.site.register(char,charAdmin)