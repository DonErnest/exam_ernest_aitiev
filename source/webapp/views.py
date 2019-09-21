from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseBadRequest

from webapp.forms import RecordForm, SearchForm
from webapp.models import Record, STATUS_DEFAULT


def index_view(request, *args, **kwargs):
    records = Record.objects.filter(status=STATUS_DEFAULT).order_by('-created_at')
    search = SearchForm()
    return render(request, 'index.html', context={'records': records, 'search': search})


def add_record(request, *args, **kwargs):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'add.html', context={'form':form})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = Record.objects.create(author=form.cleaned_data['author'],
                                           text=form.cleaned_data['text'],
                                           author_email=form.cleaned_data['author_email'])
            return redirect('book_main')
        return render(request, 'add.html', context={'form': form})


def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        form = RecordForm(data={'author': record.author, 'author_email': record.author_email,
                                'text': record.text})
        return render(request, 'edit.html', context={'form': form, 'record': record})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data['author']
            record.author_email = form.cleaned_data['author_email']
            record.text = form.cleaned_data['text']
            record.save()
            return redirect('book_main')
        else:
            return render(request, 'edit.html', context={'form': form, 'record': record})


def delete_record(request, pk, *args, **kwargs):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'record': record})
    elif request.method == 'POST':
        record.delete()
    return redirect('book_main')


def search_record(request):
    search = SearchForm(data=request.GET)
    if search.is_valid():
        text = search.cleaned_data['search_text']
        records = Record.objects.filter(author__icontains=text.lower())
        return render(request, 'search_results.html', context={'records': records, 'text': text})
    else:
        return render(request, 'search_results.html',context={'text': None})
