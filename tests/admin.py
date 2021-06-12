from django.contrib import admin

from .models import (
    cementCompressive,
    NewProject,
    cementConsistencyTest,
    cementCompressive,
    cementSettingTime,
)


admin.site.register(cementCompressive)
admin.site.register(NewProject)
admin.site.register(cementConsistencyTest)
admin.site.register(cementSettingTime)
# admin.site.register(cementCompressive)
