from datetime import datetime as dt
import csv
import xlwt 
from tempfile import TemporaryFile

read_file = open("/Users/ifeanyiokoli/Downloads/Rawfile.txt", mode = "r", encoding= "utf-8")

whole_data = read_file.readlines()
# print(whole_data[:5])
# print(len(whole_data))

# TO CLEAN DATA
for num in range(len(whole_data)):
    whole_data[num] = whole_data[num].rstrip("\n")

# print(whole_data[:5])

# TO GET THE UNIQUE DATES
unique_dates = []
for entry in whole_data:
    date = entry.split(" on ")[1]
    if date in unique_dates:
        pass
    else:
        unique_dates.append(date)

# print (unique_dates[:5])

# SORTING THE UNIQUE DATES
sorted_unique_dates = sorted(unique_dates, key = lambda a : dt.strptime(a, "%d-%m-%Y"))
# print(sorted_unique_dates[:20])


# TO SORT THE WHOLE DATA
sorted_whole_data = []
for date in sorted_unique_dates:
    for entry in whole_data:
        if date == entry.split(" on ")[1]:
            sorted_whole_data.append(entry)
        else:
            pass

# print(sorted_whole_data[:10])

# TO UNPACK THE ENTRIES
list_of_name = []
list_of_sales = []
list_of_dates = []

for entry in sorted_whole_data:
    extracted_name = entry.split(" : ")[0]
    list_of_name.append(extracted_name)

    extracted_amount = entry.split(" on ")[0].split(" : ")[1]
    refined_amount = int(extracted_amount.lstrip("₦"))
    list_of_sales.append(refined_amount)

    extracted_date = entry.split(" on ")[1]
    list_of_dates.append(extracted_date)




# WRITING THE SORTED WHOLE DATA TO A CSV FILE
# new_file = open("/Users/ifeanyiokoli/Downloads/slippo.csv", mode= "w", encoding = "utf-8", newline = "") 


# pen = csv.writer(new_file)
# pen.writerow(["Name", "Sales", "Dates"])

# for num in range(len(sorted_whole_data)):
#     pen.writerow([list_of_name[num], list_of_sales[num], list_of_dates[num]])

# new_file.close()


# PREPARING DATA FOR THE SECOND SHEET
unique_agents = sorted(list(set(list_of_name)))
print(len(unique_agents))

all_agent_sales = []

for agent in unique_agents:
    agent_sum = 0
    for index, entry in enumerate(list_of_name):
        if agent == entry:
            desired_amount = list_of_sales[index]
            agent_sum += desired_amount
        else:
            pass

    all_agent_sales.append(agent_sum)

total_revenue = sum(all_agent_sales)

impact_list = [(entry/ total_revenue)* 100 for entry in all_agent_sales]

commission_list = [0.045 * entry for entry in all_agent_sales]


# PREPARING DATA FOR THIRD SHEET
total_revenue = sum(all_agent_sales)

total_commission = sum(commission_list)

profit = total_revenue - total_commission

# WRITING TO AN EXCEL BOOK

book = xlwt.Workbook()

first_sheet = book.add_sheet("All Transactions")
second_sheet = book.add_sheet('Agents' 'Transaction')
third_sheet = book.add_sheet("Financial Statement")

# WRITING INTO FIRST SHEET
first_sheet.write(0, 0, 'Name')
first_sheet.write(0, 1,'Sales')
first_sheet.write(0, 2, 'Date')

for index, entry in enumerate(list_of_name):
    first_sheet.write(index + 1, 0, entry)

for index, entry in enumerate(list_of_sales):
    first_sheet.write(index + 1, 1, entry)

for index, entry in enumerate(list_of_dates):
    first_sheet.write(index + 1, 2, entry)


# writing into second sheet
second_sheet.write(0, 0, "Agent Name")
second_sheet.write(0, 1, "Agent Sales")
second_sheet.write(0, 2, "Impact")
second_sheet.write(0, 3, "Commission")

for index, entry in enumerate(unique_agents):
    second_sheet.write(index + 1, 0, entry)
for index, entry in enumerate(all_agent_sales):
    second_sheet.write(index + 1, 1, entry)
for index, entry in enumerate(impact_list):
    second_sheet.write(index + 1, 2, "{0:.2f}%".format(entry))
    
for index, entry in enumerate(commission_list):
    second_sheet.write(index + 1,3, entry)

    

# writing into third sheet
third_sheet.write(0, 0, "Total Revenue")
third_sheet.write(0, 1, "Total Commission")
third_sheet.write(0, 2, "Profit")


third_sheet.write(1, 0, total_revenue)
third_sheet.write(1, 1, total_commission)
third_sheet.write(1, 2, profit)

# saving the book as a file
book.save("/Users/ifeanyiokoli/Downloads/slippo_excel.xls")
book.save(TemporaryFile())


# BOTTOM FIVE
bottom_5_agent = sorted(zip(unique_agents, all_agent_sales), key=lambda el: el[1])[:5]
print(bottom_5_agent)

# MONTH WIHT THE HIGHEST AND LOWEST
refined_list_date =  [dt.strptime(i, '%d-%m-%Y') for i in list_of_dates]
refined2 = [i.strftime('%B') for i in refined_list_date]
refined_dates = list(zip(refined2, list_of_sales))
unsorted_month = {}
for k, v in refined_dates:
    unsorted_month[k] = unsorted_month.get(k, 0) + v
result = sorted(unsorted_month.items(),key=lambda a: a[1])[-1]
result_2 = sorted(unsorted_month.items(),key=lambda a: a[1])[0]
# print(unsorted_month)
print(result)
print(result_2)

    
# DATE WITH MOST SALE
refined_date_sales = zip(list_of_dates, list_of_sales)
unique_date_sale = {}
for k, v in refined_date_sales:
    unique_date_sale[k] = unique_date_sale.get(k, 0) + v
result = sorted(unique_date_sale.items(),key=lambda a: a[1])[-1]
day_most_sale = result
print(day_most_sale)
sorted(unsorted_month.items(), key= lambda a: a[1], reverse= True)

# # TOP TEN AGENTS
new_structure = zip(unique_agents, all_agent_sales)
sorted_structure = sorted(new_structure, key= lambda a : a[1], reverse= True)
for i in sorted_structure[:10]:
    print(i[0])

for i, k in sorted_structure[:10]:
    print(i)
