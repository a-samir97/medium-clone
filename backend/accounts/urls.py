from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('social/', views.SocialAccountsAPIView.as_view(), name='social'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('reset-password/',
         views.ResetPassword.as_view(), name='reset-password'),
    path('confirm-password/<uuid:user_uuid>/',
         views.ConfirmPassword.as_view(), name='confirm-password'),
    path('toggle-follow/<str:username>/',
         views.ToggleFollowAPIView.as_view(), name='toggle-follow'),
    path('following-users/', views.FollowingAPIView.as_view(),
         name='following-users'),
    path('followers-users/', views.FollowersAPIView.as_view(),
         name='followers-users'),
]
