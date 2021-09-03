import pymysql

connection = pymysql.connect(host="localhost",
                            user = "root",
                            password = "",
                            db = "JUMIA",
                            charset = "utf8mb4",
                            cursorclass = pymysql.cursors.DictCursor)

def create_table():
    with connection.cursor() as Cursor:
        create_table_smart_phones =""" 
                            CREATE TABLE IF NOT EXISTS smart_phones(
                                id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                phone_brand VARCHAR(60) NOT NULL,
                                specifications VARCHAR(255) NOT NULL,
                                old_price INT(10),
                                new_price INT(10) NOT NULL,
                                ratings FLOAT(10,4) NOT NULL
                            );
        """

        Cursor.execute(create_table_smart_phones)
        connection.commit()


def write_report(current_phone_brand,current_specifications,price,current_sales,current_ratings):
    with connection.cursor() as Cursor:
        add_report = f""" INSERT INTO smart_phones(phone_brand,specifications,old_price,new_price,ratings)
                            VALUES('{current_phone_brand}','{current_specifications}',{price}, {current_sales}, {current_ratings});

        """

        Cursor.execute(add_report)
        connection.commit()

create_table()



