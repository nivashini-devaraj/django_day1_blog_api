from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
from .views import blog_list
from .views import blog_delete
from .views import blog_edit
from .views import blog_create

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')


urlpatterns = [
    path('', include(router.urls)),
    path('blogs-page/', blog_list, name='blog-list-page'),
    path('blogs/delete/<int:id>/', blog_delete, name='blog-delete-page'),
    path('blogs/edit/<int:id>/', blog_edit, name='blog-edit-page'),
    path('blog-create/', blog_create, name='blog-create-page'),
]
