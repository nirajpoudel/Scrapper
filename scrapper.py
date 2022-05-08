from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

#chrome driver path.
path = "/home/niraj/Documents/chromedriver_linux64/chromedriver"

categories = ['national','valley','opinion','money','sports','art-culture',"politics"]
print("====================================")
print(categories)
print("====================================")
cat = input("Select a category from about you want to hear for: ")

options = Options()
#options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://kathmandupost.com/" + cat)

with open("data1.json","w") as f:
    json.dump([],f)

def write_json(new_data, filename='data1.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def main_functin():
    loadMore=False
    while not loadMore:
        try:
            elem = driver.find_element(By.CLASS_NAME,'block--morenews')
            items = elem.find_elements(By.CLASS_NAME,'article-image ')
            for item in items:
                try:
                    link = item.find_element(By.TAG_NAME,'a').get_attribute('href')
                    title = item.find_element(By.TAG_NAME,'h3').text
                    author = item.find_element(By.CLASS_NAME,'article-author').text
                    driver.find_element(By.XPATH,'//*[@id="mainContent"]/main/div/div[2]/div[1]/span/span').click()
                    print("----------------------------")
                    print(
                            {
                            "Title:",title,
                            "Author: ", author,
                            "Link:",link
                            }
                        )
                    print('----------------------------')

                except Exception as e:
                    print("Error is: " + e)
                write_json({
                    "Title": title,
                    "Author": author,
                    "Link": link
                })
                
        except:
            loadMore=True
            print("Your requirements completed!!")        

main_functin()

    