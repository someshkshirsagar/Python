"""
URL configuration for regex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import(
    include,
    path
)

from rest_framework import routers
from api.views import EntryViewSet

entry_list=EntryViewSet.as_view({
    'get':'list',

    # 'post':'create',

})
entry_detail=EntryViewSet.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    # 'put':'update',
    'delete':'destroy',
})

urlpatterns = [
    path('entries/', entry_list, name='entry-list'),
    path('entries/<int:pk>/', entry_detail, name='entry-detail' ),
]
