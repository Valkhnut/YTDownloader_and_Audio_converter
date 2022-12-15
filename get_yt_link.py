import pytube


GET_YT_LINK = input('Put YT link here: ')
YT_VIDEO_DATA = pytube.YouTube(GET_YT_LINK)
#CHANNEL_INFO = pytube.Channel(GET_YT_LINK)
