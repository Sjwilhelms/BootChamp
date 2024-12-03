from .models import Post, Comment, Profile
from django import forms
# form for user submitted new posts
class PostForm(forms.ModelForm):
    # Add a file input field for the image
    featured_image = forms.ImageField(
        required=False,  # Make the image optional
        help_text="Upload a featured image for your post"
    )

    class Meta:
        model = Post
        fields = ("title", "subtitle", "content", "featured_image", "excerpt")

    def clean_featured_image(self):
        # Optional: Add custom validation for the image
        image = self.cleaned_data.get('featured_image')
        if image:
            # Check image size, type, etc.
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image size should not exceed 5MB")
            return image
        return None

# form to comment on posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body", )

# form to update profile
class ProfileForm(forms.ModelForm):
    featured_image = forms.ImageField(
        required=False,  # Make the image optional
        help_text="Upload a featured image for your post"
    )

    
    class Meta:
        model = Profile
        fields = ("tagline", "bio", "profile_picture", )

    def clean_featured_image(self):
        # Optional: Add custom validation for the image
        image = self.cleaned_data.get('featured_image')
        if image:
            # Check image size, type, etc.
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image size should not exceed 5MB")
            return image
        return None