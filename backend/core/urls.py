from django.urls import path, include
from simple_orm.urls import urlpatterns

urlpatterns = [
    path('orm/', include(urlpatterns))
]
