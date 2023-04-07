from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import ImageDeleteView

urlpatterns = [

                  path('', views.home, name="home"),
                  path('section/<str:pk>/', views.sectionDetail, name="section-detail"),
                  path('topics/', views.sectionsPage, name="sections"),
                  path('create-section/', views.createSection, name="create-section"),
                  path('process/<str:pk>/', views.process, name="process"),
                  path('download-excel/', views.download_excel, name='download_excel'),
                  path('delete-section/<str:pk>/', views.deleteSection, name="delete-section"),
                  path('section/<str:pk>/delete-image/<int:image_id>/', ImageDeleteView.as_view(), name='delete-image'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
