from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("task-list/", views.cementList, name="cement-list"),
    path("cement-detail/<str:pk>/", views.cementDetail, name="cement-detail"),
    path("cement-create/", views.cementCreate, name="cement-create"),
    path("cement-update/<str:pk>/", views.cementUpdate, name="cement-update"),
    path("cement-delete/<str:pk>/", views.cementDelete, name="task-delete"),
]
