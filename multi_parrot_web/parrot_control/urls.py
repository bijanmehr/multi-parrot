from django.conf.urls import url,include
from django.urls import path
from parrot_control import views
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register('parrot/control',views.ParrotCommandController,'Parrot')

urlpatterns = [
    url('parrot/control', views.ParrotCommandController.as_view())
    # url('', include(router.urls)),
]
