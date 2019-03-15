
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from records import views

from mStudent import settings

admin.site.site_header = "mStudent Staff Dashboard"
admin.site.site_title = "mStudent"
admin.site.index_title = 'Dashboard'


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', admin.site.urls),
    path('api/login/', views.login),
    path('api/student/<int:id>', views.get_student)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
