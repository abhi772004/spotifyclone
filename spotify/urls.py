from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'spotify'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('artist/<int:artist_id>/', home.as_view(), name='artist_detail'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
