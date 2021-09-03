import pymysql

connection = pymysql.connect(host = "localhost",
                             user = "root",
                             password = "",
                             db = "slippo",
                             charset = "utf8mb4",
                             cursorclass = pymysql.cursors.DictCursor)

def create_table():
    with connection.cursor() as Cursor:
        create_table_activity_report = """
                            CREATE TABLE IF NOT EXISTS activity_report (
                                id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(60),
                                sales BIGINT(15),
                                `date` DATE
                                 
                             );
        
        """
        Cursor.execute(create_table_activity_report)

        connection.commit()



def write_report(current_name, current_amount, current_date):
    with connection.cursor() as Cursor:
        add_report = f"""
                    INSERT INTO activity_report (name, sales, `date`)
                    VALUES
                    ('{current_name}', {current_amount}, '{current_date}');
        """
        Cursor.execute(add_report)

        connection.commit()


create_table()