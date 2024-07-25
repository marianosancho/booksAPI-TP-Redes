import requests
import json


HOST: str = 'http://localhost'
PORT: str = '8000' 

url =  HOST + ':' + PORT



def get_all_books(): 
    response = requests.get(f"{url}/all_books")
    if response.status_code == 200:
        data: dict = json.loads(response.text)
        print(json.dumps(data, indent=4))
    return response.status_code, response.text



def get_book_by(author : str | None = None, country: str | None = None, language: str | None = None, title: str | None = None, year: int | None = None):

    request_url: f"{url}/get_book_by"
    
    if author != None:       
        request_url = request_url +  "?author=" + author.replace(" ", "%20") 

    if country != None:
        request_url = request_url +  "?country=" + country.replace(" ", "%20") 
    
    if language != None:
        request_url = request_url +  "?language=" + language.replace(" ", "%20")    

    if title != None:
        request_url = request_url +  "?title=" + title.replace(" ", "%20")

    if year != None:
        request_url = request_url +  f"?year={year}"


#get_all_books()