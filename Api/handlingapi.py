import requests

def fetch_request_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
    response = requests.get(url)
    print(f"HTTP Status Code: {response.status_code}")  
    data = response.json()
    print(f"Response Data: {data}")  

    if data.get("success") and "data" in data:
        jokes = data["data"]
        for joke in jokes:
            
            print(f"content: {joke['content']}")
            
        return jokes

    else:
        raise Exception("Failed to fetch joke")

def main():
    try:
        jokes = fetch_request_joke()
        print(jokes)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

  
  

    
    
    


  
  
  
  
  