from django.contrib import admin
from .models import Todo

admin.site.site_header = 'Miran-To do app'
admin.site.site_title = 'Miran Admin Area'
admin.site.index_title = 'Welcome to the  Miran Admin Area'


admin.site.register(Todo),