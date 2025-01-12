from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.signUp, name="signup"),
    path('login', views.logIn,name="login"),
    path('change_password', views.changepassword,name="changepassword"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('profile', views.profile,name="profile"),
    path('logout', views.LogOut,name="logout"),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name = 'passwordreset.html'),name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name= 'passwordresetdone.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='passwordresetconfirm.html'),name="password_reset_confirm"),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'),name="password_reset_complete"),

]

