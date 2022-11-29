import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import Post, Author, Category


class PostFilter(FilterSet):
    posted = django_filters.DateFilter(label='Дата публикации не ранее', lookup_expr='gt', widget=DateInput(attrs={'type': 'date'}))
    title = django_filters.CharFilter(label='Заголовок содержит', lookup_expr='icontains')
    author = django_filters.ModelMultipleChoiceFilter(label='Автор', queryset=Author.objects.all())
    category = django_filters.ModelMultipleChoiceFilter(label='Категории', queryset=Category.objects.all())
    type = django_filters.ChoiceFilter(label='Тип публикации', choices=Post.TYPES)

    # class Meta:
    #     model = Post
    #     fields = {
    #          'type': ['exact'],
    #     }
