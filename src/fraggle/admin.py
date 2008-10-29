from django.contrib import admin

from fraggle.models import Fragment

class FragmentOptions(admin.ModelAdmin):
    search_fields = ['title','content']
    list_display = ('id','title',)
    ordering = ['id']
    class Media:
        css = { 
        'all': (
				'/assets/css/admin.css',
                ) 
        }
try:
    admin.site.register(Fragment, FragmentOptions)
except admin.sites.AlreadyRegistered:
    pass