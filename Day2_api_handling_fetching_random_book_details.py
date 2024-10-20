import requests

def fetch_randombook_api_details():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()
    if data["statusCode"] == 200:
        print("connection established")
        print(data["statusCode"])
        book_data = data["data"]
        country_name = book_data["accessInfo"]["country"]
        return country_name
    else:
        raise Exception("Failed to fetch books data")
    

def main():
    try:
        country_name = fetch_randombook_api_details()
        print("Book Origin Country name is",country_name)
        
    except Exception as e:
        print(str(e))
    

if __name__ == "__main__":
    main()
    
