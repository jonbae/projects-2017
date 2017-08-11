import requests
from lxml import html

USERNAME = "*********@gmail.com"
PASSWORD = "******"

LOGIN_URL = "https://www.yelp.com/login"
URL = "https://www.yelp.com/user_details?userid=zON8jzT6Zblc3jfh4CNXCw"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrftok']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    print result.url
    print ('Jonathan' in result.text)

if __name__ == '__main__':
    main()
