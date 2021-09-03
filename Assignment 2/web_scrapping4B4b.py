import requests
from bs4 import BeautifulSoup
import csv


headers = requests.utils.default_headers()

headers.update({
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/91.0.4472.114 Safari/537.36"

})
mined_data = []

for i in range (1, 51):
    url1 = f"https://www.jumia.com.ng/smartphones/?page={i}#catalog-listing"
    url2 = "https://www.jumia.com.ng/smartphones/"
    if i == 1:
        url = url2
    else:
        url = url1

    my_response = requests.get(url, headers)

    child_soup = BeautifulSoup(my_response.content, features = 'lxml')

    first_search = child_soup.find("div", attrs= {"class" : "-paxs row _no-g _4cl-3cm-shs"})

    second_search = first_search.find_all("article", attrs = {"class" : "prd _fb col c-prd"})

    new_file = open("/Users/ifeanyiokoli/Desktop/Python/DATA SCIENCE/jumia_smartphone2.csv", mode = "w", encoding = "utf-8", newline= "")

    pen = csv.writer(new_file)
    # THE HEADER
    pen.writerow(["Phone Brand", "Phone specification", "Old Price", "New Price", "Rating" ])
    
    for soup in second_search:
        inner_container = soup.find("a")
        # FOR PHONE BRAND
        try:
            phone_brand = inner_container["data-brand"]
        except:
            phone_brand = None
        # FOR PHONE specification
        try:
            phone_specification = inner_container["data-name"]
        except:
            phone_specification = None
        # FOR OLD PRICE
        try:
            third_search = inner_container.find("div", attrs = {"class" : "old"})
            old_value = third_search.text
            if "," in old_value:
                step_one = old_value.lstrip("₦ ")
                step_two = step_one.replace("," , "" )
                old_price = int(step_two)
            else:
                step_one = old_value.lstrip("₦ ")
                old_price = int(step_one)
        except:
            old_price = None
        # NEW PRICE
        try:
            fourth_search = inner_container.find("div", attrs = {"class" : "prc"})
            new_value = fourth_search.text
            if "," in new_value:
                step_one = new_value.lstrip("₦ ")
                step_two = step_one.replace("," , "" )
                new_price = int(step_two)
            else:
                step_one = new_value.lstrip("₦ ")
                new_price = int(step_one)
        except:
            new_price = None
        # FOR RATING
        try:
            fifth_search = inner_container.find("div", attrs = {"class" : "stars _s"})
            rating_entry = fifth_search.text
            step_one = rating_entry.split(" out ")[0]
            phone_rating = float(step_one)

        except: 
            phone_rating = None
        mined_data.append([phone_brand, phone_specification, old_price, new_price, phone_rating])

    pen.writerows(mined_data)

    new_file.close()

jumia_data = mined_data
jumia_data1 = [(i[0], i[1][:10], i[2], i[3],i[4]) for i in jumia_data]



