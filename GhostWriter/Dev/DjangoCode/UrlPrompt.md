Here is some code that implements URLs that work with a Django data model for PrometaUser:


from django.contrib import admin
from django.urls import include, path

from .views import PrometaUserDeleteView, PrometaUserDetailView, PrometaUserListView, PrometaUserUpdateView, AccountSignUpView, AccountUpdateView, PrometaUserView


urlpatterns = [
    
    # PrometaUser
    path('user/',                       PrometaUserListView.as_view(),    name='user_list'),
    path('user/add',                    PrometaUserCreateView.as_view(),  name='user_add'),
    path('user/<int:pk>',               PrometaUserDetailView.as_view(),  name='user_detail'),
    path('user/<int:pk>/',              PrometaUserUpdateView.as_view(),  name='user_edit'),
    path('user/<int:pk>/delete',        PrometaUserDeleteView.as_view(),  name='user_delete'),

]

Please use this example to generate a set of URLs for a Student data model using the URL prefix "student".
