from django.contrib import admin;
from django.conf import settings;
from django.conf.urls.static import static
from django.urls import path,include;
from users import views as user_view;
from django.contrib.auth import views as auth_views;
#password rest => password rest done => password rest confirn => password rest #complete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_view.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="registeration/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="registeration/logout.html"),name="logout"),
    path('profile/',user_view.profile,name="profile"),
    path('',include('blog_app.urls')),
    path('password-rest/',auth_views.PasswordResetView.as_view(template_name="registeration/password-rest.html"),name="password_reset"),
    path('password-rest/done',auth_views.PasswordResetDoneView.as_view(template_name="registeration/password-rest-done.html"),name="password_reset_done"),
    path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registeration/password-rest-confirm.html"),name="password_reset_confirm"),
    path('password-rest/complete',auth_views.PasswordResetCompleteView.as_view(template_name="registeration/password-rest-complete.html"),name="password_reset_complete"),
    path('password/change',auth_views.PasswordChangeView.as_view(template_name="registeration/password_change.html"),name="password_change"),
    path('password/change/done',auth_views.PasswordResetDoneView.as_view(template_name="registeration/password_change_done.html"),name="password_change_done"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT);
