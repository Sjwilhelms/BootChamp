from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from cloudinary.uploader import upload
from .forms import PostForm, CommentForm, ProfileForm
from .models import Post, Comment, Profile, Like

# Models for viewing all posts on the home page and for viewing each post on it's own page
class PostList(generic.ListView):
    """
    Displays list of posts"
    """
    model = Post

def post_detail(request, slug):
    """
    Display an individual :model:'forum.post'.

    **Context**

    ``post``
        an instance of :model:'forum.post'.capitalize
    ``comments``
        all approved comments related to the post.
    ``comment_count``
        a count of approved comments related to the post
    ``comment_form``
        an instance of :form:`forum.CommentForm`
    **Template:**

    :template:'forum/post_detail.html'
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method ==  "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment submitted and awaiting approval"
            )

    comment_form = CommentForm()

    return render(
        request, 
        "forum/post_detail.html", 
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context:**
    ``post``
        an instance of :model:`forum.Post`
    ``comment``
        A single comment related to the post
    ``comment_form``
        An instance of :form:`forum.CommentForm`
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context:**
    ``post``
        An instance of :model:`forum.post`
    ``comment``
        A single comment related to the post
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(request, messages.ERROR, "You can only delete your own comments!")
    return HttpResponseRedirect(reverse("post_detail", args=[slug]))

# views pertaining to creating a post

def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            # Handle Cloudinary image upload
            if form.cleaned_data.get('featured_image'):
                # Upload image to Cloudinary
                upload_result = upload(form.cleaned_data['featured_image'])
                post.featured_image = upload_result['secure_url']
            
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})

    
# views pertaining to profile

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile  # Using the related_name='profile'
    posts = Post.objects.filter(author=user).order_by('-created_on')  # Latest posts first
    comments = Comment.objects.filter(author=user).order_by('-created_on')  # Latest comments first
    return render(
        request, 
        'forum/profile_view.html', 
        {'profile': profile,
        'posts': posts,
        'comments': comments,}
        )


