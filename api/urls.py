from django.urls import path,re_path
from .views import UserView,UserListView,UserFilerAgeView,UserListNameView,UserPdfListView

urlpatterns = [
    re_path(r'^users_age/(?P<age>\d+)$', UserFilerAgeView.as_view()),
    re_path(r'^users', UserListView.as_view()),
    re_path(r'^users/(?P<id>\d+)$', UserView.as_view()),

    re_path(r'^users_order_name', UserListNameView.as_view()),
    re_path(r'^users_pdf', UserPdfListView.as_view())
]
