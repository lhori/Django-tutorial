from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/<num>
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/<num>/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/<num>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]