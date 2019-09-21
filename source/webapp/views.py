from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseBadRequest

from webapp.forms import RecordForm
from webapp.models import Record, STATUS_DEFAULT


def index_view(request, *args, **kwargs):
    records = Record.objects.filter(status=STATUS_DEFAULT).order_by('-created_at')
    return render(request, 'index.html', context={'records': records})


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