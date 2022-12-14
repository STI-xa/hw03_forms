from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = (
            'Нужно что-то обязательно написать, иначе, не работает 😎'
        )
        self.fields['group'].empty_label = (
            'Выберите группу по интересам 🙂'
        )

    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {'text': 'Текст поста', 'group': 'Группа'}
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост',
        }
