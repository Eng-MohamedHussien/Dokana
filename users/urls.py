#from django.urls import path
#from django.contrib.auth import views as auth_views

#from . import views

app_name = 'users'

urlpatterns = [
    '''
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='delivery/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='delivery/password_reset_confirm.html', success_url = reverse_lazy('delivery:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name ='password_reset_complete')
    '''
]
