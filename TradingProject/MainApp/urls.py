import imp
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Data),
    path('json',views.BuildJson,name='BuildJson'),
    # path('admin/', admin.site.urls),
]
