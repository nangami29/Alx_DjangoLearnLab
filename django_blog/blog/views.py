from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserUpdateForm, ProfileUpdateForm, CommentForm
from django.contrib import messages
from .models import Post, Comment, Tag
from rest_framework import filters, generics
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name =  "registration/signup.html"


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect( "profile")
         # handle password update securely
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 and password1 == password2:
            user_form.set_password(password1)  
            messages.success(request, "Password updated successfully!")
        
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "blog/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })


class PostListView(ListView):
    model = Post
    template_name='blog/postlist.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

# shows detail of one post
class PostDetailView(DetailView):
    model = Post
    template_name='blog/post_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post = self.get_object()
        context['average_rating']=post.get_average_rating()

# a class_based view for updating details of a specific book
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        #Runs after the form is validated and before saving.
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

    #implement comment views to handle Crud operations
    #listview to list comments
class CommentListView(ListView):
    model= Comment
    template_name= 'blog/commentlist.html'
    context_object_name='comments'
    ordering=['_created_at_']

    #create comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name= 'blog/createcomment.html'
    form_class=CommentForm

    # N;B it saves the form (creates/updates the object) and then redirects to get_success_url().
    def form_valid(self, form):
        post_id=self.kwargs['pk']
        post = Post.objects.get(pk=post_id)
        form.instance.post =post 
        return super().form_valid(form)
    
    def get_success_url(self):
        
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})
    
# Delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model =Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('comment-list')

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'blog/updatecomment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post = self.get_object().post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    #serializer_class= UserSerializer
    filter_backends= [filters.SearchFilter]
    search_fields = ['title', 'content', 'tags']
    def get_queryset(self):
        queryset = User.objects.all()
        search_query = self.request.query_params.get('search', None)

        if search_query:
            queryset = queryset.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query)
            )

        return queryset
    
def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'posts/posts_by_tag.html', {'tag': tag, 'posts': posts})


def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct() if query else Post.objects.none()

    return render(request, 'posts/search_results.html', {'query': query, 'posts': posts})

   