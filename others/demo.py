from bs4 import BeautifulSoup
import requests
import json

with open("dump.json","w") as f:
    json.dump([],f)

def write_json(new_data, filename='dump.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def main_request():
    for page in range(1,4):
        url = 'https://krishionline.com/news/category/english-news/page/'

        r = requests.get(url+str(page))

        soup = BeautifulSoup(r.content, 'html.parser')
        content = soup.find_all('div',class_='row row-eq-height herald-posts')
        #print(content)

        for property in content:
            print(len(property))
            title = property.find('h2').text
            desc = property.find('div',class_='entry-content').text
            date = property.find('span', class_='updated').text
            print(title,desc,date)
'''
            info = {
                        'Title': title,
                        'Desc': desc,
                        'Date': date,
                        
                    }
            print(info)

  
            write_json({
                        'Title': title,
                    'Desc': desc,
                    'Date': date,
                    
                    })

'''
main_request()

