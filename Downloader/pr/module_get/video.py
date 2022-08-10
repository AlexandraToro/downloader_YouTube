from pytube import YouTube

def get_video(url, filename, path='download'):
    yt = YouTube(url)
    r = yt.streams.filter(resolution="720p").first().download(path, filename)
