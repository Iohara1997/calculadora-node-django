from django.contrib import admin
from django.urls import path, include
from calculator.views import CalculatorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'numbers', CalculatorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/', include(router.urls)),
]
