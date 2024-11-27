from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`post.Post`
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    

class Like(models.Model):
    """
    Stores a single like entry related to :model:`auth.User` and :model:`post.Post` and :model:`comment.Comment`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        target = self.post or self.comment
        return f"{self.user.username} liked {target}"

class Profile(models.Model):
    """
    Stores a single profile entry related to :model:`auth.User`
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    tagline = models.CharField(max_length=200, unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username