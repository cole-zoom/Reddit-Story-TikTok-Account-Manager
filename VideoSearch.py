from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('Minecraft Parkour Gameplay NO COPYRIGHT', limit = 10)

links = videosSearch.result()['result']

for link in links:
    print(link['link'])