from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.bemvindo, name='bemvindo'),
 	url(r'^login/$', auth_views.LoginView.as_view(template_name="Login.html"), name='login'),
    #url(r'^logout/$',auth_views.LoginView.as_view(template_name="Login.html"), name='logout'),
    url(r'^logout', views.pagelogout, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('criar_item/', views.item_new, name='item_new'),
	path('objeto/<int:pk>/edit/', views.item_edit, name='item_edit'),
	path('meus_itens/', views.meusitens, name='meus_itens'),
	url(r'^home',views.home, name='home'),
	#path('objeto/<int:pk>', views.objeto_detail, name='objeto_detail'),
	path('objeto/<int:pk>/', views.objeto_detail, name='objeto_detail'),
    #url(r'^objeto/(\d+)/', views.objeto_detail, name='objeto_detail'),
    url(r'^pedido/(\d+)/', views.pedido_detail, name='pedido_detail'),
    url(r'^usuario/(\d+)/', views.usuario_detail, name='usuario_detail'),
]
