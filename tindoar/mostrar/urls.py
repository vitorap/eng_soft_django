from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.bemvindo, name='bemvindo'),
	path('profile', views.meu_profile, name='meu_profile'),
	path('fazer_pedido/<int:pk>', views.fazer_pedido, name='fazer_pedido'),
	path('edit_user/<int:pk>', views.edit_user, name='edit_user'),
	path('ver_user/<int:pk>', views.ver_user, name='ver_user'),
	path('ver_pedidos', views.ver_pedido, name='ver_pedido'),
	path('ver_seus_pedidos', views.ver_seus_pedido, name='ver_seus_pedido'),
	path('aceitar_pedidos/<int:pk>', views.aceitar_pedidos, name='aceitar_pedidos'),
	path('recusar_pedidos/<int:pk>', views.recusar_pedidos, name='recusar_pedidos'),
 	url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout', views.pagelogout, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('criar_item/', views.item_new, name='item_new'),
	path('objeto/<int:pk>/edit/', views.item_edit, name='item_edit'),
	path('objeto/<int:pk>/delete/', views.item_delete, name='item_delete'),
	path('meus_itens/', views.meus_itens, name='meus_itens'),
	url(r'^home',views.home, name='home'),
	path('objeto/<int:pk>/', views.objeto_detail, name='objeto_detail'),
	url(r'^usuario/(\d+)/', views.usuario_detail, name='usuario_detail'),
	url(r'^doado', views.item_doado, name='doado_sucesso'),
	url(r'^sobre', views.sobre_nos, name='sobre_nos'),
	path('NLsobre', views.sobre_nos_noLogin, name='NLsobre'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)