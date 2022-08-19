import module_get
import tkinter as tk


# -*- coding: utf-8 -*-


def download():
    window = tk.Tk()
    window.geometry('600x200')
    window.title("Downloader")

    label = tk.Label(text="Введите URL - адрес страницы: ", font=("Times New Roman", 14))
    url = tk.Entry()
    label.grid(column=0, row=1)
    url.grid(
        column=1,
        row=1,
        padx=10,
        pady=10,
        ipadx=60,
        ipady=5
    )

    label = tk.Label(text="Введите название файла: ", font=("Times New Roman", 14))
    filename = tk.Entry()
    label.grid(column=0, row=2)
    filename.grid(
        column=1,
        row=2,
        padx=10,
        pady=10,
        ipadx=60,
        ipady=5
    )

    button1 = tk.Button(
        text="Скачать видео файл",
        bg='#008080',
        fg="white",
        font=("Times New Roman", 12),
        command=lambda: module_get.get_video(url, filename)
    )
    button1.grid(
        column=0,
        row=6,
        padx=10,
        pady=10,
        ipadx=30,
        ipady=5
    )

    button2 = tk.Button(
        text="Скачать аудио файл",
        bg='#4682B4',
        fg="white",
        font=("Times New Roman", 12),
        command=lambda: module_get.get_audio(url, filename)
    )
    button2.grid(
        column=1,
        row=6,
        padx=10,
        pady=10,
        ipadx=30,
        ipady=5
    )

    window.mainloop()

    # url = input('Введите URL - адрес страницы: ')
    # n = int(input('Для сохранения видео нажмите 1, для сохранения аудио-дорожки нажмите 2: '))
    # filename = input('Введите название файла: ') + ".mp4"
    # if n == 1:
    #     module_get.get_video(url, filename)
    # else:
    #     module_get.get_audio(url, filename)
