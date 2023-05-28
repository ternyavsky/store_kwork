from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordResetView, PasswordChangeDoneView

urlpatterns = [
    path('accounts/login/',views.LoginView.as_view(),name='login'),
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('accounts/logout/',views.Logout,name='logout'),
    path('passwordreset/',views.Passwordresetview.as_view(),name='passwordreset'),
    path('reset/<uidb64>/<token>/',views.Passwordchangeview.as_view(),name='passwordchange'),
    path('account/<int:id>',views.acc,name='acc'),
    path('accounts/edit/<int:id>',views.edit,name='edit'),
    path('accounts/delete/<int:id>',views.delete_account,name='delete_account'),

]