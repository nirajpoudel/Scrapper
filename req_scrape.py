from bs4 import BeautifulSoup
import requests
import json


categories = ['World','Business','Opinion','Sports',"Entertainment"]
print("====================================")
print(categories)
print("====================================")
cat = input("Select a category from about you want to hear for: ")

with open("dump.json","w") as f:
    json.dump([],f)

def write_json(new_data, filename='dump.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def main_request():
    for page in range(1,30):
        url = 'https://thehimalayantimes.com/morearticles/{0}?pgno='.format(cat)

        r = requests.get(url+str(page))

        all_info = []
        soup = BeautifulSoup(r.content, 'html.parser')
        content = soup.find_all('div',class_='post_list post_list_style_1')
        for property in content:
            try:
                title = property.find('h3').text
                desc = property.find('div',class_='alith_post_except VisibleMobile fontsize14height40').text
                date = property.find('span', class_='meta_date').text
                type = property.find('span',class_='section').text

                info = {
                    'Title': title,
                    'Desc': desc,
                    'Date': date,
                    'Type':type
                }
                print(info)
                write_json({
                        'Title': title,
                    'Desc': desc,
                    'Date': date,
                    'Type':type
                    })
                
            except:
                pass

main_request()