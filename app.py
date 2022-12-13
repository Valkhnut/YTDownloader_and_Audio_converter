import pytube


YT_LINK = input('Put YT link here: ')
YT_VIDEO_DATA = pytube.YouTube(YT_LINK)


def get_filename(yt_data):
    file_name = yt_data.title
    return file_name


def get_yt_streams(yt_data):
    yt_stream = yt_data.streams.filter(file_extension='mp4')
    return yt_stream


def download_stream(yt_data):
    stream = yt_data.streams.get_by_itag(22)
    return stream.download()


print(get_yt_streams(YT_VIDEO_DATA))


download_stream(YT_VIDEO_DATA)
