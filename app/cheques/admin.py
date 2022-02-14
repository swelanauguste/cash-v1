from django.contrib import admin

from .models import Cheque, ChequeComment

admin.site.register(Cheque)
admin.site.register(ChequeComment)
