from django.urls import path

from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('<int:pk>', ProfileDetailView.as_view(), name='profile_id'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='profile_id_update'),
]
