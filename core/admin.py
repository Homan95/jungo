from django.contrib import admin
from .models import feeed, Bots, Autor

# Register your models here.

@admin.register(feeed)		
class feeedsADMIN(admin.ModelAdmin):
	list_display=('name','text','is_active','created')
	list_editable=('is_active',)


@admin.register(Bots)
class feeedsADMIN(admin.ModelAdmin):
	list_display=('bot_name','name','is_active')
	list_editable=('is_active',)

@admin.register(Autor)
class feeedsADMIN(admin.ModelAdmin):
	list_display=('name','email','webpage')
	