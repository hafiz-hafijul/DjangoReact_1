from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.PostView)

urlpatterns = [
    path("viewapi/",include(router.urls)),
    path("setapi/", views.ApiView, name="setapi"),
    path("strapi/<str:pk>/", views.strApi, name="strapi"),
]


