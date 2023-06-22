from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers = headers).text
    content = BeautifulSoup(response, "html.parser")

    all_title = content.find_all("span", attrs={"class": "title"})

    for item in all_title:
        title_string = item.string
        if "/" not in title_string:
            print(title_string)