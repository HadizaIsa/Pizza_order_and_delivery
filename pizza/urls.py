from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Pizza Delivery API",
      default_version='v1',
      description="Pizza order and delivery api",
      terms_of_service="https://www.google.com/policies/terms/",
      incontact=openapi.Contact(email="adma@gmail.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('orders/', include('orders.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema_json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]
