from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


'''
Tutorial: https://likegeeks.com/es/web-scraping-beautiful-soup-y-selenium/
Do scrapping in the title of python.org
HTTPError: for error 404 (page not found) or 500 (error in server)
URLError: for error in url
'''
def scraping():
    try:
        html = urlopen("https://www.python.org/")
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        res = BeautifulSoup(html.read(),"html5lib")
        #tags = res.findAll("span")
        tags = res.span.findAll("class")
        for tag in tags:
            print(tag)


def main():
    scraping()

if __name__ == "__main__":
    main()