from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('', views.home, name="home"),
                  path('section/<str:pk>/', views.sectionDetail, name="section-detail"),
                  path('topics/', views.sectionsPage, name="sections"),
                  path('create-section/', views.createSection, name="create-section"),
                  path('process/<str:pk>/', views.process, name="process"),
                  path('download-excel/', views.download_excel, name='download_excel'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
