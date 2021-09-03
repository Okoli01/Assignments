from jumia_db_functions import *
import csv

jumia_data = []
def read_and_send_data():
    # new_file = open(r"/Users/ifeanyiokoli/Desktop/Python/DATA SCIENCE/jumia_smartphone2.csv", mode= "r", encoding= "utf-8")

    new_file = csv.reader(r"/Users/ifeanyiokoli/Desktop/Python/DATA SCIENCE/jumia_smartphone2.csv", skipinitialspace = True)
    print(list(new_file[:2]))


    # header = new_file.readlines(1)
    # whole_doc = new_file.readlines()
    # print(whole_doc[:2])

    # refined_doc = [entry.rstrip("\n") for entry in whole_doc]
    
    # for entry in refined_doc:
    #     entry = entry.split(",")

    #     print(entry[0])
    #     print(entry[1])
    #     print(entry[2])
    #     print(entry[3])
    #     print(entry[4])

    #     break
        # write_report(entry[0], entry[1], int(entry[2]), int(entry[3]), float(entry[4]))
        
read_and_send_data()