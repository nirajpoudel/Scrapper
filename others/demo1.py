from multiprocessing import Condition
from bs4 import BeautifulSoup
from numpy import tile
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
    url = 'https://krishionline.com/news/category/english-news/'

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    
    content = soup.find_all('div',class_='herald-module herald-main-content col-lg-9 col-md-9')
    con = True

    while con:
        for property in content:
            title = property.find('h2',class_='entry-title h3').text

       
            print(title)
        '''
        desc = property.find('div',class_='entry-content').text
        date = property.find('span', class_='updated').text
            

        info = {
                'Title': title,
                'Desc': desc,
                'Date': date    
            }
        print(info)
        
            write_json({
                    'Title': title,
                'Desc': desc,
                'Date': date,
                
                })
            
        except:
            pass
'''
main_request()