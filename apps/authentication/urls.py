from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import RegistrationEndpoint

urlpatterns = [
    path('auth/registration/', view=RegistrationEndpoint.as_view()),
    path(
        'auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
]
