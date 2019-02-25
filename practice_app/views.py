from django.shortcuts import render, get_object_or_404, redirect
from .models import Writing
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import SongLyrics

def new(request):
    return render(request, 'new.html')

def main(request):
    songs = Writing.objects
    songs_list = Writing.objects.all()
    paginator = Paginator(songs_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'main.html',{'writings': songs, 'posts':posts})
# Create your views here.

def more(request,song_id):
    song_lyrics = get_object_or_404(Writing,pk = song_id)

    return render(request, 'lyrics.html',{'song':song_lyrics})

def create(request):
    song = Writing()
    song.title = request.GET['title']
    song.body = request.GET['lyrics']
    song.pub_date = timezone.datetime.now()
    song.save()
    return redirect('/lyrics/'+str(song.id))

def portfolio(request):
    return render(request, 'portfolio.html')

def songpost(request):
    if request.method == 'POST':
        form = SongLyrics(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = SongLyrics()
        return render(request, 'new.html', {'form':form})
    
