from django.shortcuts import render, get_object_or_404, redirect
from news.models import Record
from django.urls import reverse
from news.forms import CommentForm, RecordForm


def records_views(request):
    search = request.GET.get('search', '')
    if search:
        records = Record.objects.filter(name__iregex=search, hidden=True)
    else:
        records = Record.objects.filter(hidden=True).order_by('-date')
    return render(request, 'news/list_records.html', {'records': records})


def records_detail(request, rec_id):
    rec = get_object_or_404(Record, id=rec_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = rec
            form.save()
            form = CommentForm()

    else:
        form = CommentForm()
    comment = rec.comments.all()
    context = {'detail': rec, 'comments': comment, 'form': form}
    return render(request, 'news/detail_records.html', context)


def records_create(request):
    if request.method == 'POST':
        form = RecordForm(data=request.POST, files=request.FILES)
        print(form.fields)
        if form.is_valid():
            form.save()
            return redirect(reverse('records:record'))
    else:
        form = RecordForm()

    context = {'form': form}
    return render(request, 'news/create_records.html', context)
