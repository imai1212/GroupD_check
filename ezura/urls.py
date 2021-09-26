from django.urls import path
from . import views

app_name = 'ezura'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('blog-list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog-create/', views.BlogCreateView.as_view(), name="blog_create"),
    path('blog-update<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog-delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),
    path('all-blog-list/', views.AllBlogListView.as_view(), name="all_blog_list"),
]
