import argparse
import sys
import os
from sys import argv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


DEVELOPER_KEY = 'AIzaSyDFwz3l_jQBdgPU7dU1cp2raVbpnE-R3pc'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(q=query, part='id,snippet', regionCode ='NZ', maxResults=max_results).execute()
    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            #videos.append('%s (%s) %s' % (search_result['snippet']['thumbnails']['high']['url'], search_result['id']['videoId'], search_result['snippet']['title']))
            videos.append('%s (%s)' % (search_result['id']['videoId'], search_result['snippet']['title']) )
    
    print ('Searched Keyword:', query)
    
    a = 0
    total_videos = len(videos)
    while a < total_videos:
        print ("".join(['https://www.youtube.com/watch?v=',videos[a]]))
        a = a+1
        continue

if __name__ == '__main__':
    youtube_search(sys.argv[1], '5')
