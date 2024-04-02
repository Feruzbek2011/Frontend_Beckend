from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name = 'post_list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('edit/<int:pk>/', PostEditView.as_view(), name = 'post_edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name = 'post_delete'),
    path('create/', PostCreateView.as_view(), name = 'post_create'),
                                    # COMMENT URL
    path('comment/detail/<int:pk>/', CommentDetailView.as_view(), name = 'comment_detail'),
    path('comment/edit/<int:pk>/', CommentEditView.as_view(), name = 'comment_edit'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name = 'comment_delete'),
    path('comment/create/<int:pk>/', CommentCreateView.as_view(), name = 'comment_create'),
]
