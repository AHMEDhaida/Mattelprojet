from django.contrib import admin

# Register your models here.
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_phone_number', 'get_image')
    list_select_related = ('profile', )

    def get_phone_number(self, instance):
        return instance.profile.phone_number
    get_phone_number.short_description = 'phone_number'

    def get_image(self, instance):
        return instance.profile.image
    get_image.short_description = 'image'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
