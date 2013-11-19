from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from markdown import markdown


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    tags = models.CharField(max_length=100)
    author = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_tags(self):
        if self.tags:
            return self.tags.split(',')
        return []

    def markdown(self):
        return markdown(self.content)

    def get_description(self):
        if len(self.excerpt) > 0:
            return self.excerpt
        return self.content[:360]

    def get_excerpt(self):
        if len(self.excerpt) > 0:
            return markdown(self.excerpt)
        return markdown(self.content[:360])

    def get_url(self):
        return reverse('blog.detail', args=[str(self.id)])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']
    

