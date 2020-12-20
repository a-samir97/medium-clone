from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt import views as jwt_views

import debug_toolbar

schema_view = get_schema_view(
   openapi.Info(
      title="Medium API",
      default_version='v1',
      description="Cloning Medium website",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [

   path('admin/', admin.site.urls),
   
   path('sentry-debug/', trigger_error),
   path('debug/', include(debug_toolbar.urls)),

   path('api-accounts/', include('accounts.urls', namespace='accounts')),
   path('api-login/', include('rest_social_auth.urls_token')),
   
   # JWT
   path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
   path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   
   path('api-posts/', include('posts.urls', namespace='posts')),
   path('api-tags/', include('tag.urls', namespace='tags')),
   path('api-comments/', include('comment.urls', namespace='comments')),
   path('api-vote/', include('vote.urls', namespace='votes')),
   path('api-collections/', include('collection.urls', namespace='collections')),

   
   # Swagger documentation
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
