import requests
from .models import Content

def create_post(request):
    data = request.POST['text']
    if data == "":
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": "Bearer API_KEY",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Create a short paragraph for the following title: {request.POST['title']}"
                    }
                ]
            }
        )

        print(response.json())
        data = response.json()['choices'][0]['message']['content']

    new_post = Content(
        title = request.POST['title'],
        text = data,
        user_id = request.user.id,
    )
    new_post.save()
