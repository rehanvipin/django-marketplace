from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def home(request):
    context = {'goods':Post.objects.all()}
    return render(request, 'market/home.html', context=context)


def about(request):
    return render(request, 'market/about.html', context={'title':'Swampert'})


class PostListView(ListView):
    # Path to template: <app>/<model>_<viewtype>.html
    model = Post
    template_name = 'market/home.html'
    # what do we call this object in the template context?
    context_object_name = "goods"
    ordering = ["-upload_date"]
    paginate_by = 4

class UserPostListView(ListView):
    # Path to template: <app>/<model>_<viewtype>.html
    model = Post
    template_name = 'market/seller_items.html'
    # what do we call this object in the template context?
    context_object_name = "goods"
    ordering = ["-upload_date"]
    paginate_by = 4

    def get_queryset(self):
        seller = get_object_or_404(User, username=self.kwargs.get('seller'))
        return Post.objects.filter(seller=seller).order_by('-upload_date')


class PostDetailView(DetailView):
    # use generic object names, update template
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['item_name', 'description', 'votes']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['item_name', 'description', 'votes']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        item = self.get_object()
        return self.request.user == item.seller


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        item = self.get_object()
        return self.request.user == item.seller