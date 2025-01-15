from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm, CommentForm, ProfileForm
from .models import Post, Comment


# for viewing all posts on the home page
class PostList(generic.ListView):
    """
    Displays list of posts"
    """

    model = Post


# views for posts and comments


def post_detail(request, slug):
    """
    Display an individual :model:'forum.post'.

    **Context**

    ``post``
        an instance of :model:'forum.post'
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
    if request.method == "POST":
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
            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment updated!"
                )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating comment!")

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
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )
    return HttpResponseRedirect(reverse("post_detail", kwargs={"slug": slug}))


# views pertaining to posts


def create_post_view(request):
    """
    Create an instance of :model:`forum.post`

    create_post.html
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("home")
        else:
            messages.error(
                request,
                "There was an error in your form submission."
            )
    else:
        form = PostForm()

    return render(request, "forum/create_post.html", {"form": form})


def edit_post_view(request, slug):
    """
    Edit a particular instance of a post by slug

    edit_post.html
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Post updated successfully!")
            return redirect("post_detail", slug=post.slug)
        else:
            messages.error(
                request,
                "There was an error in your form submission."
            )
    else:
        form = PostForm(instance=post)
    return render(
        request,
        "forum/edit_post.html",
        {"form": form, "post": post}
        )


def delete_post_view(request, slug):
    """
    Delete a particular instance of a post by slug
    """
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post deleted successfully!")
    return redirect("home")


# views pertaining to profile


def profile_view(request, username):
    """
    View a particular instance of a profile by username,
    showing also posts and comments

    profile_view.html
    """
    user = get_object_or_404(User, username=username)
    profile = user.profile
    posts = Post.objects.filter(author=user).order_by("-created_on")
    comments = Comment.objects.filter(author=user).order_by("-created_on")
    return render(
        request,
        "forum/profile_view.html",
        {
            "profile": profile,
            "posts": posts,
            "comments": comments,
        },
    )


# view to edit custom profile


def edit_profile_view(request):
    """
    Edit the signed in users own profile page

    edit_profile.html
    """
    profile = request.user.get_or_create_profile()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile", username=request.user.username)
    else:
        # populates form with current values
        form = ProfileForm(instance=profile)
    return render(request, "forum/edit_profile.html", {"form": form})
