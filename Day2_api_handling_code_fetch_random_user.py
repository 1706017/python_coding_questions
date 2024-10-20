import requests

def fetch_random_user_fromapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json() #converting the response to json
    
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["country"]
        return user_name,user_country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username,country = fetch_random_user_fromapi()
        print(f"Username: {username} \n Country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
    
        
        
    
    
