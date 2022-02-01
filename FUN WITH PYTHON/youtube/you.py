import pytube
def downloadvideo(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_audio_only()
    video.download()

downloadvideo('https://youtu.be/YyVI46K8q9E')