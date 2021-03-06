import mysql.connector
import pandas as pd

try:
    read_file = pd.read_excel ("gogo.xlsx")
    #columns= ['order_no','trans_date','st_name'] excel file column header
    # Write the dataframe object
    # into csv file
    read_file.to_csv ("Test.csv",
    				index = None,
    				header=True)

    # Import CSV
    data = pd.read_csv (r'Test.csv')   
    df = pd.DataFrame(data, columns= ['order_no','trans_date','st_name'])

    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='')
    
    mySql_Drop_Table_Query = """DROP TABLE IF EXISTS Persons;"""

    mySql_Create_Table_Query = """CREATE TABLE Persons (
                                    id int NOT NULL AUTO_INCREMENT,
                                    order_no int NOT NULL,
                                    trans_date varchar(255),
                                    st_name varchar(255),
                                    PRIMARY KEY (id)
                                );  """
    
    mySql_Insert_Query = """INSERT INTO Persons (order_no, trans_date, st_name)
                            VALUES (%s, %s, %s)"""
    
    
    cursor = connection.cursor()
    result = cursor.execute(mySql_Drop_Table_Query)
    print("Persons Table DROPED successfully ")
    result = cursor.execute(mySql_Create_Table_Query)
    print("Persons Table created successfully ")
    
    # Insert DataFrame to Table
    for row in df.itertuples():
        cursor.execute(mySql_Insert_Query,
                (row.order_no, 
                row.trans_date,
                row.st_name
                ))
    connection.commit()
    
    

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
