from bs4 import BeautifulSoup
from urllib.request import urlopen

def search_movie(name):
    name = name.replace(' ', '+')
    url = f'http://metalmovies.tk/?s={name}'
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    
    articles = soup.find_all('article')
    
    movies = {}
    for article in articles:
        title = article.div.div.a.string.replace('دانلود فیلم ', '')
        link = article.div.div.a['href']
        movies[title] = link
    
    return movies

def get_download_links(movie_link:str):
    page = urlopen(movie_link)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    
    links = soup.find_all('a', {'class': 'link_dl'})
    
    dl_links = {}
    for link in links:
        title = link.i.string
        href  = link['href']
        dl_links[title] = href
    
    return dl_links
