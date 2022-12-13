import pytube


YT_LINK = input('Put YT link here: ')
YT_VIDEO_DATA = pytube.YouTube(YT_LINK)
