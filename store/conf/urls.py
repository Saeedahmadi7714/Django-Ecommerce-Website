from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('api_core.api.urls')),
                  path('', include('products.urls')),
                  path('customer', include('customers.urls')),
                  path('order/', include('orders.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
