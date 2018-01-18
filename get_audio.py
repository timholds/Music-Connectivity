from pytube import YouTube

link = 'https://www.youtube.com/watch?v=n57YaOvuSu0'
yt = YouTube(link)
print('hey world')

yt.streams.filter(only_audio=True).first().download()
print(yt.streams.filter(only_audio=True).all())
print('done')


def convert_to_aac(stream, file_handle):
    pass
    # do work
#yt.register_on_complete_callback(convert_to_aac)

def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    pass
    # do work
yt.register_on_progress_callback(show_progress_bar)