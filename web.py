from flask import Flask
import scrapper

app = Flask(__name__)


@app.route('/search/<movie_name>')
def search_movie(movie_name):
    movies = scrapper.search_movie(movie_name)
    out = ''
    for name, link in movies.items():
        link = f'http://127.0.0.1:5000/movie/{link}'
        out = out + f"<a href='{link}'>{name}</a><br>"


    return out

@app.route('/movie/<address>')
def movie_links(address):
    links = scrapper.get_download_links(address)
    out = ''
    for name, link in links.items():
       out = out + f"<a href='{link}'>{name}</a><br>"
    
    return out



if __name__ == '__main__':
   app.run(debug = True)
