from bs4 import BeautifulSoup
import requests
import json

#creating a json file for storing the data.
with open("final.json","w") as f:
    json.dump([],f)

#writing into the json file. 
def write_json(new_data, filename='final.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

#getting all the news links for pagination.
def get_links(page):
    url = f'https://myrepublica.nagariknetwork.com/category/sports?page={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = []
    content = soup.find_all('div',class_="categories-list-info")

    for items in content:
        links.append("https://myrepublica.nagariknetwork.com"+items.find('a').attrs['href'])
    return links

#finding title and whole news description by entering inside each news details
def parse_news(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    contents = soup.find_all('div',class_="box recent-news-categories-details")
    for value in contents:
        #catching error if the news title and description doesnot exists.
        try:
            news_title = value.find('h2').text.strip().replace('\n','')
            detail_news = value.find('div',id="newsContent").text.strip().replace('\n','')

        except Exception as err:
            news_title = None
            detail_news = None
            print(news_title,detail_news)
        new = {
            "Title": news_title,
            "Desc":detail_news
        }
        #writing news_title and description to json file using write_json function.
        write_json({
                            'Title': news_title,
                        'Desc': detail_news,
                        
                        })
    return new

def main():
    results = []
    #Testing for 3 pages.
    for x in range(755,757):
        print("Current Page: ",x)
        urls = get_links(x)
        if urls:
            for url in urls:
                results.append(parse_news(url))
        else:
            print("No urls found")
            break
        print('Total number of news extracted: ',len(results))

if __name__=='__main__':
    main()

