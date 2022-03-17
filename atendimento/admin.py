from django.contrib import admin

from atendimento.models import assunto, atender, publico, tipo

admin.site.register(publico)
admin.site.register(tipo)
admin.site.register(assunto)
admin.site.register(atender)
