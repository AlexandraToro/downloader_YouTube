import module_get


def download():
    url = input('Введите URL - адрес страницы: ')
    n = int(input('Для сохранения видео нажмите 1, для сохранения аудио-дорожки нажмите 2: '))
    filename = input('Введите название файла: ') + ".mp4"
    if n == 1:
        module_get.get_video(url, filename)
    else:
        module_get.get_audio(url, filename)
