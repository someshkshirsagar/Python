from django.contrib import admin
from .models import Entry
from .models import UserProfile , TestString

# Register your models here.
#admin.site.register(Entry)
#@admin.register(Entry) this can also be use 
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    autocomplete_fields=['test_string']
    list_display=[
        'pattern',
     #   'test_strings',
        'user'
    ]
    list_filter=['user']
    list_filter=['test_string']

@admin.register(TestString)
class TestAdmin(admin.ModelAdmin):
    list_display=[
        "string"
    ]
    search_fields=['string']


