QUALITY_SETTINGS = {  # num: itag
    '1': 160,  # (144p) Didn't work in default player
    '2': 133,  # (240p) Didn't work in default player
    '3': 18,   # (360p)
    '4': 135,  # (480p) Didn't work in default player
    '5': 22,   # (720p)
    '6': 137,  # (1080p) Didn't work in default player
}

VIDEO_QUALITY = {  # itag: quality
    160: '144p',
    133: '240p',
    18: '360p',
    135: '480p',
    22: '720p',
    137: '1080p',
}


def choose_quality():
    print('''Choose quality of video for downloading: 
    1. 144p
    2. 240p
    3. 360p
    4. 480p
    5. 720p
    6. 1080p
     
    Enter num from 1 to 6:''')
    quality = input()
    try:
        QUALITY_SETTINGS[quality]
    except KeyError:
        print("Fatal Error. Try again!")
        choose_quality()
    else:
        yt_itag = (QUALITY_SETTINGS[quality])
        return yt_itag


itag = choose_quality()


def yt_stream_downloader(yt_data):
    stream = yt_data.streams.get_by_itag(itag)
    return stream.download(f'Downloads/{VIDEO_QUALITY[int(itag)]}')
