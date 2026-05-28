from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'providers', views.ProviderViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'commands', views.CommandViewSet)
router.register(r'admins', views.AdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
]