from django.shortcuts import render
from .forms import VideoForm, VisitorsComment
from .models import video, comments
from django.http import HttpResponse

# Create your views here.
def index(request):
    videos=video.objects.all()
    comment=comments.objects.all()
    if request.method == 'POST':
        form=VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Your video has been uploaded successfully!')
    else:
        form=VideoForm()

    if request.method == 'POST':
        comment_form=VisitorsComment(request.POST)
        if comment_form.is_valid():
            visitor_comment = comment_form.save(commit=False)
            visitor_comment.videos = videos
            visitor_comment.save()
            return HttpResponse('Thank you for your comment.')
    else:
        comment_form=VisitorsComment()

    return render(request, 'home.html', {'form':form,'all':videos, 'comment_form':comment_form, 'comment':comment})


