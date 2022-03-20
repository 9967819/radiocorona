from django.contrib import admin

# Register your models here.
from radiocorona.frontend.admin import SubmissionInline
from radiocorona.users.models import RedditUser


class RedditUserAdmin(admin.ModelAdmin):
    inlines = [
        SubmissionInline,
    ]

admin.site.register(RedditUser, RedditUserAdmin)
