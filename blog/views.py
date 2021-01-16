from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post


class LoginStaffRequired(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BlogListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginStaffRequired, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    login_url = 'home'


class BlogUpdateView(LoginStaffRequired, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    login_url = 'home'


class BlogDeleteView(LoginStaffRequired, DeleteView):  # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'home'
