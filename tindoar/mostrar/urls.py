from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.bemvindo, name='bemvindo'),
	path('profile', views.meu_profile, name='meu_profile'),
 	url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout', views.pagelogout, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('criar_item/', views.item_new, name='item_new'),
	path('objeto/<int:pk>/edit/', views.item_edit, name='item_edit'),
	path('objeto/<int:pk>/delete/', views.item_delete, name='item_delete'),
	path('meus_itens/', views.meus_itens, name='meus_itens'),
	url(r'^home',views.home, name='home'),
	path('objeto/<int:pk>/', views.objeto_detail, name='objeto_detail'),
    url(r'^pedido/(\d+)/', views.pedido_detail, name='pedido_detail'),
    url(r'^usuario/(\d+)/', views.usuario_detail, name='usuario_detail'),
]
