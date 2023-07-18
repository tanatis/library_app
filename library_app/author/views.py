from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from library_app.author.forms import AuthorEditForm, AuthorDeleteForm, AuthorCreateForm
from library_app.author.models import Author
from library_app.core.functionality import get_creator_user


class AuthorCreateView(views.CreateView):
    model = Author
    template_name = 'author/author_create.html'
    form_class = AuthorCreateForm
    #fields = ('name', 'bio', 'birth_year', 'death_year', 'nationality', 'picture',)

    success_url = reverse_lazy('index')

    # Access only to Creators
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name='Creator').exists():
            return redirect('restricted')
        return super().dispatch(request, *args, **kwargs)


@login_required
@user_passes_test(get_creator_user, login_url='restricted')
def author_edit(request, pk):
    author = Author.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AuthorEditForm(instance=author)
    else:
        form = AuthorEditForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author details', pk=author.pk)
    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'author/author_edit.html', context)


def author_details(request, pk):
    author = Author.objects.filter(pk=pk).get()
    context = {
        'author': author,
        'author_books': author.book_set.all(),
    }
    return render(request, 'author/author_details.html', context)


def author_delete(request, pk):
    author = Author.objects.filter(pk=pk).get()
    form = AuthorDeleteForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'author/author_delete.html', context)


def list_authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/list_authors.html', context)
