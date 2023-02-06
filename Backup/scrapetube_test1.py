import scrapetube

#videos = scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g")
videos = scrapetube.get_channel("UCO-n4ZDDXKPKK29c5eaytpA")


for video in videos:
    for x in video['label']:
        print(x)
    print("------------------")
   