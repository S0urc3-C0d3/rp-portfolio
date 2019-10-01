from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Your Name"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Leave a comment!"}))

class PostForm(forms.Form):
    author = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Your Name"}))
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Title of your post!"}))
    body = forms.CharField(widget=forms.Textarea({"class": "form-control", "placeholder": "Write a new Post"}))
    category = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Which category does your post refer to?"}))
    tags = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Type in some tags that describe your post (separated by comma)"}))

class AddCategory(forms.Form):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Add new Category"}))