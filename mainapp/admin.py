from django.contrib import admin

from .models import Home, Hometext, About, AboutText, Mavzu, Images, Video, Contact

# Register your models here.

admin.site.register(Home)
admin.site.register(Hometext)
admin.site.register(About)
admin.site.register(AboutText)
admin.site.register(Mavzu)
admin.site.register(Images)
admin.site.register(Video)
admin.site.register(Contact)

