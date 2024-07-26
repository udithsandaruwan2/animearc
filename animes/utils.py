from bs4 import BeautifulSoup as bs
import requests

def getAnimeList(url):
    page = requests.get(url)
    content = page.content
    soup = bs(content, "html.parser")
    li_tags = soup.find_all('li')


    episodes = []


    for li in li_tags:
        a_tag = li.find('a')
        if a_tag:
            link = a_tag.get('href')
            title_tag = a_tag.find('div', class_='epl-title')
            if title_tag:
                title = title_tag.text.strip()
                episodes.append({'link': link, 'title': title})
    
    return episodes

def getEpi(url):

    response = requests.get(url)

    # Parse the HTML content of the webpage
    soup = bs(response.content, 'html.parser')

    # Find the div with the class "video-content"
    video_content_div = soup.find('div', class_='video-content')

    # Find the meta tag with the itemprop attribute set to "embedUrl"
    embed_url_meta = video_content_div.find('meta', itemprop='embedUrl')

    # Extract the content attribute of the meta tag, which contains the video URL
    video_url = embed_url_meta['content'] if embed_url_meta else None
    return video_url