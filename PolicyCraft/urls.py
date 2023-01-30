"""PolicyCraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from administrator import views
from company import com_views
from user import user_views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    #---------------------ADMIN PATHS---------------------------#
    path('admin_header_footer/', views.admin_header_footer),
    path('admin_home/', views.admin_home),
    path('approve_company/', views.approve_company),
    path('approve_com/', views.approve_com),
    path('view_company/', views.view_company),
    path('remove_com/', views.remove_com),
    path('approve_user/', views.approve_user),
    path('approve_us/', views.approve_us),
    path('view_user/', views.view_user),
    path('remove_us/', views.remove_us),
    path('add_category/', views.add_category),
    path('admin_view_policy/', views.admin_view_policy),


    #---------------------Company PATHS---------------------------#
    path('com_header_footer/', com_views.com_header_footer),
    path('com_home/', com_views.com_home),
    path('premium/', com_views.premium),
    path('insurance_amount/', com_views.insurance_amount),
    path('add_policy/', com_views.add_policy),
    path('view_policy/', com_views.view_policy),
    path('view_request/', com_views.view_request),
    path('remove_policy/', com_views.remove_policy),
    path('update_status/', com_views.update_status),
    path('pay_history/', com_views.pay_history),
    path('view_user/', com_views.view_user),
    path('complaint/', com_views.complaint),


 #---------------------User PATHS---------------------------#
    path('user_header_footer/', user_views.user_header_footer),
    path('user_home/', user_views.user_home),
    path('user_view_policy/', user_views.user_view_policy),
    path('apply_policy/', user_views.apply_policy),
    path('status/', user_views.status),
    path('list_policy/', user_views.list_policy),
    path('policy_form/', user_views.policy_form),
    path('remove_appl/', user_views.remove_appl),
    path('payment1/', user_views.payment1),
    path('payment2/', user_views.payment2),
    path('payment3/', user_views.payment3),
    path('payment4/', user_views.payment4),
    path('payment5/', user_views.payment5),
    path('view_pay_history/', user_views.view_pay_history),
    path('rate_now/', user_views.rate_now),
    

]
