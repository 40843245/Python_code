from youtube_search import YoutubeSearch

"""
results = YoutubeSearch('search terms', max_results=10).to_json()

print("----------------------------")
for x in results:
    print(x)
"""
# returns a json string

########################################

results = YoutubeSearch('search terms', max_results=10).to_dict()

print("----------------------------")
for x in results:
    print(x)
# returns a dictionary