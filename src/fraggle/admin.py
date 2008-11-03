from django.contrib import admin

from fraggle.models import Fragment

class FragmentOptions(admin.ModelAdmin):
    "Provides a more useful admin interface that the django default"
    search_fields = ['title','content']
    list_display = ('id','title',)
    ordering = ['id']
    fieldsets = (
        (None,
            {'fields':('title','content')}
        ),
        ('Hidden',
            {
                'fields':('html',),
                'classes':('collapse',),                
            }
        ),
    )
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