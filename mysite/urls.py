from customer.views import TestView
from django.contrib import admin
from django.urls import include, path

from customer.views import TestView

urlpatterns = [
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('customer.urls')),
    path('admin/', admin.site.urls),
    path('testview/', TestView.as_view(), name = "Data Customer")
]