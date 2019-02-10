from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuizList.as_view()),
]
    # path('<int:pk>/', views.QuizDetail.as_view()),