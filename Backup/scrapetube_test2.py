import scrapetube

videos = scrapetube.get_channel("UCO-n4ZDDXKPKK29c5eaytpA")


for video in videos:
    print(video['videoId'])
    print()
    