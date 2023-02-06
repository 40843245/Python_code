import scrapetube
import webbrowser


base_YT_watch_url="https://www.youtube.com/watch?v="
videos = scrapetube.get_channel("UCO-n4ZDDXKPKK29c5eaytpA")

for video in videos:
    print(video['videoId'])
    #webbrowser.open(base_YT_watch_url+video['videoId'])
    