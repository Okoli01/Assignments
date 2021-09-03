import requests
import csv
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()

### SCRAPING IN DISGUISE ####
headers.update({
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.3"
})


url = "https://www.nairaland.com"

my_response =  requests.get(url, headers)

child_soup = BeautifulSoup(my_response.content, features = "lxml")

# print(child_soup)

first_search = child_soup.find("td", attrs = {"class" : "featured w"})

# print(first_search)

second_search = first_search.find_all("a")

# print(second_search)

new_file = open("/Users/ifeanyiokoli/Desktop/Python/nairaland.csv",mode = "w", encoding = "utf-8", newline = "")

pen = csv.writer(new_file)

###THE HEADER###
pen.writerow(["S/N", "News Headline", "Number Of Views"])
mined_data = []

# print(second_search)

for index, soup in enumerate(second_search):
    index += 1
    # print(soup.prettify())
    headlines = soup.text
    new_url = soup["href"]


    new_response = requests.get(new_url, headers)
    new_soup = BeautifulSoup(new_response.content, features = "lxml")
    
    further_search = new_soup.find("p", attrs = {"class" : "bold"})

    number_of_views = int(str(further_search).split("</a>")[-1].split("</p>")[0].strip(" ()").split(" ")[0])

    mined_data.append([index, headlines, number_of_views])

    

pen.writerows(mined_data)
new_file.close()