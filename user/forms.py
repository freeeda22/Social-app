from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tags
        fields = "__all__"

class StoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        fields = "__all__"

class PostimageForm(forms.ModelForm):
    
    class Meta:
        model = PostImage
        fields = "__all__"

class PoststatusForm(forms.ModelForm):
    
    class Meta:
        model = PostStatus
        fields = "__all__"