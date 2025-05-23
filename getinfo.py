import requests
import re
import sys

def get_tiktok_user_info(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    html_content = response.text

    patterns = {
        "User ID": r'"webapp.user-detail":{"userInfo":{"user":{"id":"(\d+)"',
        "Username": r'"uniqueId":"(.*?)"',
        "Nickname": r'"nickname":"(.*?)"',
        "Followers": r'"followerCount":(\d+)',
        "Following": r'"followingCount":(\d+)',
        "Likes": r'"heartCount":(\d+)',
        "Videos": r'"videoCount":(\d+)',
        "Biography": r'"signature":"(.*?)"',
        "Verified": r'"verified":(true|false)',
        "SecUid": r'"secUid":"(.*?)"',
        "Comment Setting": r'"commentSetting":(\d+)',
        "Private Account": r'"privateAccount":(true|false)',
        "Region": r'"region":"(.*?)"',
        "Heart": r'"heart":(\d+)',
        "Digg Count": r'"diggCount":(\d+)',
        "Friend Count": r'"friendCount":(\d+)',
        "Profile Picture URL": r'"avatarLarger":"(.*?)"'
    }

    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, html_content)
        if match:
            value = match.group(1)
            if key == "Nickname":
                value = value.replace("'", "\\'")
            if key == "Profile Picture URL":
                value = value.replace('\\u002F', '/')
            results[key] = value
        else:
            results[key] = f"No {key.lower()} found"

    print("User Information:")
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python getinfo.py <username>")
    else:
        get_tiktok_user_info(sys.argv[1])