from django import forms
from . import models


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = models.ArticleColumn
        fields = ('column',)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = models.ArticlePost
        fields = ('title', 'body')


class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = models.ArticleTag
        fields = ('tag',)
