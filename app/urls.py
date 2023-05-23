from django.urls import path
from . import views
from .views import generate_pdf


app_name = 'app'

urlpatterns = [
    path('', views.cover, name='cover'),
    path('title', views.title, name='title'),
    path('subtitle/', views.subtitle, name='subtitle'),
    path('boardtitle', views.boardtitle, name='boardtitle'),
    path('boardelement/', views.boardelement, name='boardelement'),
    path('preview/', views.preview, name='preview'),
    path('template/', views.template, name='template'),
    # path('download-pdf/', views.download_pdf, name='download_pdf'),
    # path('pdf/', MyPDFView.as_view(), name='download_pdf'),
    path('pdf/', generate_pdf, name='download_pdf'),
]