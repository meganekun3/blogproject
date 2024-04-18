from django.urls import path
from blog.views import PostList, PostCreateView

urlpatterns = [
    path("", PostList.as_view()),
    path("create/", PostCreateView.as_view())
]