from apiclient.discovery import build 
   
# Arguments that need to passed to the build function 
DEVELOPER_KEY = 'AIzaSyDFwz3l_jQBdgPU7dU1cp2raVbpnE-R3pc'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
   
# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
   
   
def youtube_search_location(query, max_results): 
    # calling the search.list method to 
    # retrieve youtube search results 
    search_location = youtube_object.search().list(q = query, type ='video', eventType ='live', part = 'id, snippet', 
                          maxResults = max_results).execute() 
       
    # extracting the results from search response 
    results = search_location.get('items', [])

    # empty list to store video metadata 
    videos = []
       
    # extracting required info 
    # from each result object 
    for result in results: 
        # video result object 
        if result['id']['kind'] == 'youtube#video':
            videos.append('%s (%s)' % (result['id']['videoId'], result['snippet']['title']))
            #videos.append('% s (% s) (% s) (% s)' % (result['snippet']['title'], 
            #                     result['id']['videoId'], result['snippet']['description'], 
            #                     result['snippet']['thumbnails']['default']['url'])) 
    a = 0
    total_videos = len(videos)
    while a < total_videos:
        print ("".join(['https://www.youtube.com/watch?v=',videos[a]]))
        #print (a, maxims)
        a = a+1
        continue

    #print 'Videos:\n', '\n'.join(videos), '\n'

if __name__ == '__main__': 
    youtube_search_location('Music', max_results = 10)
