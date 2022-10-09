from django.urls import path

from users.views import login_view, registration_view, logout_view, ProfileView

app_name = 'users'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]