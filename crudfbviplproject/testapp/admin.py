from django.contrib import admin
from testapp.models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display=['pno','pname','psal','paddr']

admin.site.register(Player,PlayerAdmin)
