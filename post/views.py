from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post, Comments
from .forms import PostForm, PostEditForm, PostCommentForm, PostCommentEditForm
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name='article/post_list.html'
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name='article/post_detail.html'
class PostEditView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name='article/post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser
class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name='article/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser

class PostCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'article/post_create.html'
    success_url = reverse_lazy('home')  # tugagach qayerga yuboriladi

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UPLOADCARE_PUBLIC_KEY'] = settings.UPLOADCARE_PUBLIC_KEY
        return context
# COMMENT

class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comments
    template_name='comment/comment_detail.html'
class CommentEditView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Comments
    form_class = PostCommentEditForm
    template_name='comment/comment_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser
    # fields = '__all__'
class CommentDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Comments
    template_name='comment/comment_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = PostCommentForm
    template_name='comment/comment_create.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.posts_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


    success_url = reverse_lazy('post_list')

# def CommentCreateView(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == "POST":
#         form = PostCommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.posts = posts
#             comment.author = request.user
#             comment.save()
#             HttpResponseRedirect(reverse("post_detail"), agrs=[post_id])
#     else:
#         form = PostCommentForm()
#
#     content = {
#         'post': post,
#         'comment': comment
#     }
#     return render(request, 'comment_create.html')
#     content = {
#         'form': form
#     }
#     return render(request, 'post_detail.html', content)
