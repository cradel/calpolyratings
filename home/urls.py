from django.urls import path, include
from . import views
from authentication import views as auth_views
from teacher_profile.views import AddTeacher
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('add-teacher/', AddTeacher.as_view(), name='add_professor'),
    path('core/', include('core.urls')),
    path('department/', include('department_courses.urls')),
    path('check_username/', auth_views.check_username, name='check_username'),
    path('accounts/', include('allauth.urls')),
    path('<slug:teacher_name>/', include('teacher_profile.urls'))
]
