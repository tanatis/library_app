from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from library_app.author.forms import AuthorEditForm
from library_app.author.models import Author


def author_create(request):
    return render(request, 'author/author_create.html')


class AuthorCreateView(views.CreateView):
    model = Author
    template_name = 'author/author_create.html'
    fields = ('name', 'bio', 'nationality',)
    success_url = reverse_lazy('index')

    # Access only to Creators
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name='Creator').exists():
            return redirect('restricted')
        return super().dispatch(request, *args, **kwargs)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Creator').exists(), login_url='restricted')
def author_edit(request, pk):
    author = Author.objects.filter(pk=pk).get()
    form = AuthorEditForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('author details', pk=author.pk)
    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'author/author_edit.html', context)


def author_details(request, pk):
    context = {
        'author': Author.objects.filter(pk=pk).get()
    }
    return render(request, 'author/author_details.html', context)


def author_delete(request, pk):
    # TODO: Author delete
    return render(request, 'author/author_delete.html')


def list_authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/list_authors.html', context)
