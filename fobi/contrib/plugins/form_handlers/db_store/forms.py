from django import forms

from fobi.contrib.plugins.form_handlers.db_store.models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)