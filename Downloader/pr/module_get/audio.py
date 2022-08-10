from pytube import YouTube


def get_audio(url, filename, path='download'):
    yt = YouTube(url)
    r = yt.streams.filter(only_audio=True).first().download(path, filename)