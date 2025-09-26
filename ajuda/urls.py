# ajuda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PedidoAjudaListView.as_view(), name='pedido-ajuda-lista'),
    path('novo/', views.PedidoAjudaCreateView.as_view(), name='pedido-ajuda-criar'),
    path('<int:pk>/', views.PedidoAjudaDetailView.as_view(), name='pedido-ajuda-detalhe'),
    path('<int:pk>/editar/', views.PedidoAjudaUpdateView.as_view(), name='pedido-ajuda-editar'),
    path('obrigado/', views.pedido_ajuda_obrigado, name='pedido-ajuda-obrigado'),
]
