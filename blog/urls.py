from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
     path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:                                                                  
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)