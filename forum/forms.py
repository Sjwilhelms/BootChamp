from .models import Post, Comment, Profile

from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "subtitle", "content", "featured_image", )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body", )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("tagline", "bio", "profile_picture", )
