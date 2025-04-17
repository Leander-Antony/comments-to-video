from googleapiclient.discovery import build
import pandas as pd
import re
import time

API_KEY = 'AIzaSyDvD_4PHCpc1_bKRiyjPh3C-34MyTylBA0'
youtube = build('youtube', 'v3', developerKey=API_KEY)

video_urls = [
    "https://www.youtube.com/watch?v=mFa13CIo2No",
    "https://www.youtube.com/watch?v=B9ou3pu3xSQ&t=6s",
    "https://www.youtube.com/watch?v=EMHb50V3Tco",
    "https://www.youtube.com/watch?v=rf71xhAqrk4",
    "https://www.youtube.com/watch?v=mS2rJ2bIzwQ&t=4598s",
    "https://www.youtube.com/watch?v=nEtmmcKYVtU",
    "https://www.youtube.com/watch?v=3FrGdO6vg6s",
    "https://www.youtube.com/watch?v=_FE_iMcSe5U",
    "https://www.youtube.com/watch?v=X955SmTm1rY",
    "https://www.youtube.com/watch?v=ialgRAC-cns",
    "https://www.youtube.com/watch?v=PGPGG3guotc&t=2252s",
    "https://www.youtube.com/watch?v=rWjky-ibZIM",
    "https://www.youtube.com/watch?v=fKjdiU0XlF4",
    "https://www.youtube.com/watch?v=R3rG6Aiwdho",
]

def get_video_id(url):
    pattern = r"(?:v=|youtu\.be/)([^&\n]+)"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_video_title(video_id):
    response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()
    return response["items"][0]["snippet"]["title"]

def get_top_comments(video_id, max_comments=2000):
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

    return sorted(comments, key=lambda x: x["likes"], reverse=True)[:5]

data = []

for url in video_urls:
    video_id = get_video_id(url)
    print(video_id)
    if not video_id:
        continue

    try:
        title = get_video_title(video_id)
        print(f"Fetching comments for: {title}")
        comments = get_top_comments(video_id)

        for comment in comments:
            data.append({
                "video_title": title,
                "comment": comment["comment"],
                "username": comment["username"],
                "likes": comment["likes"]
            })

        time.sleep(1) 

    except Exception as e:
        print(f"Error processing {url}: {e}")

df = pd.DataFrame(data)
df.to_csv("sidemen_top_comments.csv", index=False)
print("Saved to sidemen_top_comments.csv")
