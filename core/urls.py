from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', auth_views.login,
    {'template_name': 'home/login.html'}, name="login"),
    url(r'^criar/conta/$', views.criarConta, name="criate"),
    url(r'^dashbord/', include("dashbord.urls")),

]
