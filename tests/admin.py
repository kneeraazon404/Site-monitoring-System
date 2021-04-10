from django.contrib import admin

from .models import cementCompressive, NewProject, cementConsistencyTest

#  cementSettingTime

admin.site.register(cementCompressive)
admin.site.register(NewProject)
# admin.site.register(cementSettingTime)
admin.site.register(cementConsistencyTest)
