from Slippo_db_functions import *


def read_and_send_data():
    new_file = open("/Users/ifeanyiokoli/Downloads/Slippo.csv", mode = "r", encoding = "utf-8")
    header = new_file.readlines(1)
    whole_doc = new_file.readlines()

    refined_doc = [entry.rstrip("\n") for entry in whole_doc]

    for entry in refined_doc:
        extracted_data = entry.split(",")
        write_report(extracted_data[0], int(extracted_data[1]), date_editor(extracted_data[2]))



def date_editor(date_to_edit):
    splitted_data = date_to_edit.split("-")
    edited_date = "-".join([splitted_data[2], splitted_data[1],splitted_data[0]])

    return edited_date

read_and_send_data()