from django.urls import path
from .views import UserListCreateView, BlockUserView, UnBlockUserView, UserToAdminView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/block', BlockUserView.as_view(), name='block_user'),
    path('/<int:pk>/unblock', UnBlockUserView.as_view(), name='unblock_user'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
]
