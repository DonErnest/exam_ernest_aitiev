from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseBadRequest


from webapp.models import Record, STATUS_DEFAULT


def index_view(request, *args, **kwargs):
    records = Record.objects.filter(status=STATUS_DEFAULT).order_by('-created_at')
    return render(request, 'index.html', context={'records': records})