from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib import messages

from library_app.author.forms import AuthorEditForm, AuthorDeleteForm, AuthorCreateForm
from library_app.author.models import Author
from library_app.core.functionality import get_creator_user


class AuthorCreateView(views.CreateView):
    model = Author
    template_name = 'author/author_create.html'
    form_class = AuthorCreateForm

    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name='Creator').exists():
            messages.error(request, 'You are not allowed to add authors')
            return redirect('restricted')
        return super().dispatch(request, *args, **kwargs)


@login_required
def author_edit(request, pk):
    if not get_creator_user(request.user):
        messages.error(request, 'You are not allowed to edit authors')
        return redirect('restricted')

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


@login_required
def author_delete(request, pk):
    if not get_creator_user(request.user):
        messages.error(request, 'You are not allowed to delete authors')
        return redirect('restricted')

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
