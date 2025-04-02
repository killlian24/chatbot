import requests

def fetch_strapi_content():
    url = "http://localhost:1337/api/artikel?populate=*"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["data"]

    texts = []
    for entry in data:
        title = entry["attributes"].get("title", "")
        content = entry["attributes"].get("content", "")
        texts.append(f"{title}\n\n{content}")
    return texts
