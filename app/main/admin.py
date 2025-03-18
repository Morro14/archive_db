from django.contrib import admin
from django.contrib.auth.models import User
from main.models import DataEntry, DataTag, DataType, MyUser

# Register your models here.


class DataEntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(MyUser)
admin.site.register(DataEntry, DataEntryAdmin)
admin.site.register(DataTag, DataEntryAdmin)
admin.site.register(DataType, DataEntryAdmin)
