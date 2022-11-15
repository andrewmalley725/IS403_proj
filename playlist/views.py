from django.shortcuts import render, redirect
from .models import Songs

# Create your views here.
def indexPageView(request):
    songs = Songs.objects.all().values()
    context = {
        'data':songs
    }
    return render(request, 'displaySongs.html', {'data':context})


def createPageView(request):
    return render(request, 'addSong.html')

def addRecordView(request):
    return redirect(indexPageView)

def editPageView(request, sid):
    song = Songs.objects.values().get(id=sid)
    context = {
        'data':song
    }
    print(context)
    return render(request, 'editSong.html', {'data':context})

def submitChanges(request,sid):
    song = Songs.objects.get(id=sid)

    if request.method == 'POST':
        name = request.POST['SongName']
        artist = request.POST['Artist']
        album = request.POST['Album']
        year = request.POST['YearReleased']

        song.SongName = name
        song.Artist = artist
        song.Album = album
        song.YearReleased = year

        song.save()
    return redirect(indexPageView)
    

def deletePageView(request, sid):
    song = Songs.objects.get(id=sid).delete()
    return redirect(indexPageView)