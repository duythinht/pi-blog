from django.contrib import admin
from models import Entry
from workbench.me.models import Track


class EntryAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'excerpt', 'tags', 'author')
    list_display = ('title', 'author', 'created')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        is_new = obj.id is None
        obj.save()

        # Auto make a track
        if is_new:
            track = Track()
            track.detector = obj.author
            track.link = obj.get_url()
            track.text = obj.title
            track.save()

    class Media:
        js = ('js/behave.js', 'js/indent.js',)

admin.site.register(Entry, EntryAdmin)

