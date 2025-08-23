from django.urls import path
from task_event.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', event_list, name='event-list'),
    path('event/create/', create_event, name='event-create'),
    path('participant/create/', create_participant, name='participant-create'),
    path('category/create/', create_category, name='category-create'),
    path('dashboard/', dashboard, name='dashboard'),
    path('search/', search_events, name='event-search'),
    path('event/<int:event_id>/update/', update_event, name='event-update'),
    path('event/<int:event_id>/delete/', delete_event, name='event-delete'),
    path('signup/', signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="event-list"), name="logout"),
]
