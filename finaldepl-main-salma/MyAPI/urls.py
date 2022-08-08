from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.CustomerView)
urlpatterns = [
    # path('api/', include(router.urls)),
    # path('status/', views.Customerreject),
    path('', views.get_request, name='cxform'),
    #path('result/', views.result, name='form')
 
]