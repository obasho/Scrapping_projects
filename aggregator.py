import requests

url = "https://news.ycombinator.com"
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    page_content = response.text
    print(page_content)
else:
    print(f"Failed to fetch content from {url}")
