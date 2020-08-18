from django.urls import path
from shorterner import views

urlpatterns = [
    path('shorturl/<int:pk>',views.shorturlview,name='shorturl'),
    path('shorturllist/',views.shorturllist,name='shorturllist'),
]
