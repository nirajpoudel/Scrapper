from bs4 import BeautifulSoup
import requests
import json

with open("new_total.json","w") as f:
    json.dump([],f)

def write_json(new_data, filename='new_total.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def news_pagination():
    for page in range(0,5):
        try:
            url = 'https://myrepublica.nagariknetwork.com/category/sports?page='
            r = requests.get(url+str(page))
            soup = BeautifulSoup(r.content, 'html.parser')
            all_info = []
            content = soup.find_all('div',class_="categories-list-info")
            print("Total number of News in page {}: ".format(page),len(content))

            for value in content:
                title = value.find('h2').text
                desc = value.find('p').findNext('p').text
                date = value.find('p').text
                
                info = {
                    "Title":title,
                    "Desc":desc,
                    "Date":date
                }
                write_json({
                            'Title': title,
                        'Desc': desc,
                        'Date':date 
                        })

                all_info.append(info)
        except Exception as e:
            print("Exception is: ",e)

news_pagination()