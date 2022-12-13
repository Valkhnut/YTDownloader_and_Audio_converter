QUALITY_SETTINGS = {
    1: 160,  # (144p) Didn't work in default player
    2: 133,  # (240p) Didn't work in default player
    3: 18,   # (360p)
    4: 135,  # (480p) Didn't work in default player
    5: 22,   # (720p)
    6: 137,  # (1080p) Didn't work in default player
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
    quality = int(input())
    try:
        quality in range(1, 7)
    except ValueError:
        print("This isn't number!")
    except TypeError:
        print('Try again!')
    except False:
        print('You must  enter num in range from 1 to 6! Try again!!!')
    else:
        yt_itag = QUALITY_SETTINGS[quality]
        return yt_itag



def yt_stream_downloader(yt_data):
    stream = yt_data.streams.get_by_itag(choose_quality())
    return stream.download('Downloads/')