from django.urls import path
from .views import PostAPIListView,PostAPCreateView

urlpatterns = [
    path('', PostAPIListView.as_view()),
    path('<int:pk>/', PostAPCreateView.as_view())
]
