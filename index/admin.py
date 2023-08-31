from django.contrib import admin

# Register your models here.

from .models import aboutnew,client,visitor
admin.site.register(aboutnew)


admin.site.register(client)
admin.site.register(visitor)