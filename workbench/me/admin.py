from django.contrib import admin
from models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'detector', 'created')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'detector', None) is None:
            obj.detector = request.user
        obj.save()


admin.site.register(Track, TrackAdmin)