from django.db import models

class Fragment(models.Model):
    """
    Represents an html fragment
    """
        
    title = models.CharField(max_length=250)
    content = models.TextField(help_text=u'Use Textile for formatting.')