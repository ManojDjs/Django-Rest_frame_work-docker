from django.contrib import admin
# Register your models here.
from posts.models import PPosts,PReplyComment,PComments

# admin.site.register(Messages)
admin.site.register(PPosts)
admin.site.register(PReplyComment)
admin.site.register(PComments)

