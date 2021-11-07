from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from conf import settings
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView, )

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('social_django.urls', namespace='social')),

    path('api/v1/', include('api_core.api.urls')),
    path('', include('products.urls')),
    path('customer/', include('customers.urls')),
    path('order/', include('orders.urls')),

    # Django urls for reset password
    path('password_reset/',
         PasswordResetView.as_view(
             template_name='customers/password_reset.html'),
         name='password_reset'),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='customers/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='customers/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(template_name='customers/password_reset_complete.html'),
         name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
