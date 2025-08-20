from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'spotify'

urlpatterns = [
    path('', home.as_view(), name='home'),
    # path('songs/', songview.as_view(), name='song_list'),
    path('artist/<int:pk>/', artistview.as_view(), name='artistdetail'),
    path('album/<int:pk>/', albumview.as_view(), name='albumdetail'),   



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
