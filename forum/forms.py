from .models import Post, Comment, Profile
from django import forms

# form for user submitted new posts


class PostForm(forms.ModelForm):

    featured_image = forms.ImageField(
        required=False, help_text="Upload a featured image for your post"
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "subtitle",
            "content",
            "featured_image",
        )

    def clean_featured_image(self):
        image = self.cleaned_data.get("featured_image")
        if image:
            if hasattr(image, "size"):
                max_size = 5 * 1024 * 1024  # 5MB
                if image.size > max_size:
                    raise forms.ValidationError(
                        "Image size should not exceed 5MB"
                        )
            return image
        return None


# form to comment on posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


# form to update profile
class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False, help_text="Upload a profile picture for your post"
    )

    class Meta:
        model = Profile
        fields = (
            "tagline",
            "bio",
            "profile_picture",
        )

    def clean_featured_image(self):

        image = self.cleaned_data.get("featured_image")
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError("Image size should not exceed 5MB")
            return image
        return None
