import imp
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Data),
    # path('admin/', admin.site.urls),
]
