from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug
from .forms import BugPostForm


def bug_list(request):
    bugs = Bug.objects.all()
    print(bugs)
    # bugs = Bug.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "list.html", {'bugs': bugs})


def bug_detail(request, id):
    bug = get_object_or_404(Bug, pk=id)
    bug.views += 1
    bug.save()
    return render(request, "detail.html", {'bug': bug})


def new_bug(request):
    if request.method == "POST":
        form = BugPostForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.issue_type = "BUG"
            bug.author = request.user
            bug.published_date = timezone.now()
            bug.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugPostForm
    return render(request, 'new_bug.html', {'form': form})


def new_feature(request):
    if request.method == "POST":
        form = BugPostForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.issue_type = "FTR"
            bug.author = request.user
            bug.published_date = timezone.now()
            bug.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugPostForm
    return render(request, 'new_feature.html', {'form': form})


def edit_bug(request, id):
    bug = get_object_or_404(Bug, pk=id)
    if request.method == "POST":
        form = BugPostForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.updated_date = timezone.now()
            bug.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugPostForm(instance=bug)
    return render(request, 'edit_bug.html', {'form': form})
