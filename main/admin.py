from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(profile)
admin.site.register(profile_image)
admin.site.register(book)
admin.site.register(book_instances)
admin.site.register(review)
admin.site.register(interest)
admin.site.register(req_user)

