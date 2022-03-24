from django.contrib import admin

from atendimento.models import assunto, atender, publico, tipo


class atender_full(admin.ModelAdmin):
    list_display = ('atendimento', 'publico', 'tipo', 'assunto')


admin.site.register(publico)
admin.site.register(tipo)
admin.site.register(assunto)
admin.site.register(atender, atender_full)
