from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path('', views.LeadListView.as_view(), name='list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.LeadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='delete'),
    path('create/', views.LeadCreateView.as_view(), name='create'),
    path('<int:pk>/assign-agent/', views.AssignAgentView.as_view(), name='assign-agent'),
]