from django.contrib import admin
from .models import Band, BandAdmin

admin.site.register(Band, BandAdmin)