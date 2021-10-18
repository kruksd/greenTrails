from django.contrib import admin


from .models import CampModel,aboutModel, instaLinkModel,Conformation, youTubeModel
admin.site.register(CampModel)
admin.site.register(aboutModel)
admin.site.register(instaLinkModel)
admin.site.register(Conformation)
admin.site.register(youTubeModel)

# Register your models here.
