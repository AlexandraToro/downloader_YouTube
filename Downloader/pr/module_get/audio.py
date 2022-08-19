import pytube


def get_audio(url, filename, path='download'):
    filename = filename.get() + ".mp4"
    url = url.get()
    yt = pytube.YouTube(url)
    r = yt.streams.filter(only_audio=True).first().download(path, filename)
