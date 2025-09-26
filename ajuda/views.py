from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PedidoAjuda

# Criar pedido de ajuda
class PedidoAjudaCreateView(LoginRequiredMixin, CreateView):
    model = PedidoAjuda
    fields = ['titulo', 'descricao']  # o usuário e status serão automáticos
    template_name = 'ajuda/form.html'
    success_url = reverse_lazy('pedido-ajuda-lista')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # vincula ao usuário logado
        return super().form_valid(form)

# Listar pedidos
class PedidoAjudaListView(LoginRequiredMixin, ListView):
    model = PedidoAjuda
    template_name = 'ajuda/list.html'
    context_object_name = 'pedidos'

# Detalhar pedido
class PedidoAjudaDetailView(LoginRequiredMixin, DetailView):
    model = PedidoAjuda
    template_name = 'ajuda/detail.html'
    context_object_name = 'pedido'

# Editar pedido (só o dono pode editar)
class PedidoAjudaUpdateView(LoginRequiredMixin, UpdateView):
    model = PedidoAjuda
    fields = ['titulo', 'descricao', 'status']
    template_name = 'ajuda/form.html'
    success_url = reverse_lazy('pedido-ajuda-lista')

    def get_queryset(self):
        # restringe para que só o usuário dono edite
        return PedidoAjuda.objects.filter(usuario=self.request.user)

# Página de agradecimento (caso queira manter)
def pedido_ajuda_obrigado(request):
    return render(request, 'ajuda/obrigado.html')
