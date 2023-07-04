from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export import resources, fields as f
from django.contrib.auth.hashers import make_password
from django.db import models

# Register your models here.

# from django.contrib.auth.models import AbstractUser
# class CustomUser(AbstractUser):
#     course_code = models.CharField(max_length=10)
#     course_name = models.CharField(max_length=10)
#     def __str__(self):
#         return self.username
class UserResource(resources.ModelResource):
    # password = f.Field(column_name='password', attribute='password')

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.password = make_password(instance.password)
        super().before_save_instance(instance, using_transactions, dry_run)

    class Meta:
        model = User
        fields = ('username','password')
        import_id_fields = ('username',)
        export_order = ('username','password')

class UserAdmin(ImportExportModelAdmin):
    list_display = ['username', 'is_staff']
    # fields=('username', 'email', 'first_name', 'last_name', 'password')
    resource_class = UserResource
# admin.site.register(CustomUser)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



from .models import Record, Stud
# admin.site.unregister(Record)
# admin.site.unregister(Stud)
admin.site.register(Record)
admin.site.register(Stud)