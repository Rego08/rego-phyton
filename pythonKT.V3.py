import requests

url = "https://dummyjson.com/comments"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    comments = data['comments']
    
    comment_id = int(input("Sisesta ID: "))
    
    for comment in comments:
        if comment['id'] == comment_id:
            print(f"Comment ID: {comment['id']}")
            print(f"Body: {comment['body']}")
            print(f"Post ID: {comment['postId']}")
            print(f"Likes: {comment['likes']}")
            print(f"User ID: {comment['user']['id']}")
            print(f"Username: {comment['user']['username']}")
            print(f"Full Name: {comment['user']['fullName']}")
            break
    else:
        print("Sellist komentaari ei ole")