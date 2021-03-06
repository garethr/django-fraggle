"Models for Fraggle fragment manager for Django"

from django.db import models
from django.contrib.markup.templatetags.markup import textile
 
class Fragment(models.Model):
    "Represents an html fragment"
    title = models.CharField(max_length=250)
    content = models.TextField(help_text=u'Use Textile for formatting.')
    html = models.TextField(blank=True, null=True)
    
    def transform_content(self):
        "Return the textile transformed content. Also found in html property."
        return textile(self.content)
        
    def save(self, force_insert=False, force_update=False):
        "On saving fragment, save textile formatted html into html property"
        self.html = textile(self.content)
        super(Fragment, self).save()