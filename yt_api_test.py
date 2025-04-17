from googleapiclient.discovery import build
import re

API_KEY = 'AIzaSyDvD_4PHCpc1_bKRiyjPh3C-34MyTylBA0'
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_id(url):
    pattern = r"(?:v=|youtu\.be/)([^&]+)"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_all_comments(video_url, max_comments=500):
    video_id = get_video_id(video_url)
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        ).execute()

        for item in response["items"]:
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "username": snippet["authorDisplayName"],
                "comment": snippet["textDisplay"],
                "likes": snippet["likeCount"]
            })

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments

yt_link = "https://www.youtube.com/watch?v=R3rG6Aiwdho"
all_comments = get_all_comments(yt_link, max_comments=2000)

top_comments = sorted(all_comments, key=lambda x: x["likes"], reverse=True)[:50]

for i, c in enumerate(top_comments, 1):
    print(f"{i}. {c['username']} ({c['likes']} likes): {c['comment']}")
