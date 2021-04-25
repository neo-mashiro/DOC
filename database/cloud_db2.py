"""
Access DB2 on Cloud using Python (for scripting)
"""

import ibm_db

# Identify the database connection credentials
dsn = "DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=cdq34813;PWD=1l7vj7-szs45d7qq;"

# Connect
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected!")
except:
    print("Unable to connect to database")

# Create a table in the database
dropQuery = "drop table INSTRUCTOR"
dropStmt = ibm_db.exec_immediate(conn, dropQuery)

createQuery = "create table INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"
createStmt = ibm_db.exec_immediate(conn, createQuery)
print(createStmt)

# Insert data into the table
insertQuery = "insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"
insertStmt = ibm_db.exec_immediate(conn, insertQuery)

insertQuery2 = "insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)

# Query data in the table
selectQuery = "select * from INSTRUCTOR"
selectStmt = ibm_db.exec_immediate(conn, selectQuery)

while ibm_db.fetch_row(selectStmt) != False:
    # ibm_db.result(sql, col_idx) extract data row by row from sql
    print(" ID:", ibm_db.result(selectStmt, 0), " FNAME:", ibm_db.result(selectStmt, "FNAME"))

# Update data in the table
ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_OFF)  # manual commit is preferred

updateQuery = "update INSTRUCTOR set CITY='MOOSETOWN' where FNAME='Rav'"
updateStmt = ibm_db.exec_immediate(conn, updateQuery)

ibm_db.commit(conn)

# Retrieve data into Pandas dataframe
import pandas
import ibm_db_dbi

pconn = ibm_db_dbi.Connection(conn)  # connection for pandas

sql = "select * from INSTRUCTOR"
df = pandas.read_sql(sql, pconn)
print(df)

# Close the Connection
ibm_db.close(conn)





"""
Access Databases with SQL Magic (for Jupyter notebooks, JupyterLab)
"""

# Requires the 'ipython-sql' extension

# Use %%sql at the top of a cell to indicate we want the entire cell to be treated as SQL.
# Use %sql followed by a sql statement to indicate we want the current line to be treated as SQL.

# List all available magic functions
%lsmagic

# Load the ipython-sql extension
import ibm_db
import ibm_db_sa
import sqlalchemy

%load_ext sql

# Connect (format: ibm_db_sa://username:password@hostname:port/database-name)
%sql ibm_db_sa://cdq34813:1l7vj7-szs45d7qq@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB

# Create table
%%sql
DROP TABLE INTERNATIONAL_STUDENT_TEST_SCORES;
CREATE TABLE INTERNATIONAL_STUDENT_TEST_SCORES (country     VARCHAR(50)
                                               ,first_name  VARCHAR(50)
                                               ,last_name   VARCHAR(50)
                                               ,test_score  INT
                                               );

%config SqlMagic.autocommit=False  # manual commit is preferred

# Insert data into table
%%sql
DELETE INTERNATIONAL_STUDENT_TEST_SCORES;
INSERT INTO INTERNATIONAL_STUDENT_TEST_SCORES (country, first_name, last_name, test_score)
     VALUES ('United States', 'Marshall', 'Bernadot', 54)
           ,('Ghana', 'Celinda', 'Malkin', 51)
           ,('Ukraine', 'Guillermo', 'Furze', 53)
           ,('Greece', 'Aharon', 'Tunnow', 48)
           ,('Russia', 'Bail', 'Goodwin', 46)
           ,('Poland', 'Cole', 'Winteringham', 49)
           ,('Sweden', 'Emlyn', 'Erricker', 55)
           ,('Russia', 'Cathee', 'Sivewright', 49)
           ,('China', 'Barny', 'Ingerson', 57)
           ,('Uganda', 'Sharla', 'Papaccio', 55)
           ,('China', 'Stella', 'Youens', 51)
           ,('Poland', 'Julio', 'Buesden', 48)
           ,('United States', 'Tiffie', 'Cosely', 58)
           ,('Poland', 'Auroora', 'Stiffell', 45)
           ,('China', 'Clarita', 'Huet', 52)
           ,('Poland', 'Shannon', 'Goulden', 45)
           ,('Philippines', 'Emylee', 'Privost', 50)
           ,('France', 'Madelina', 'Burk', 49)
           ,('China', 'Saunderson', 'Root', 58)
           ,('Indonesia', 'Bo', 'Waring', 55)
           ,('China', 'Hollis', 'Domotor', 45)
           ;

# Control transaction
%sql commit;
%sql rollback;

# Using Python variables in your SQL statements
# You can use python variables in your SQL statements by adding a ":" prefix to your python variable names.
country = "China"
%sql select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = :country

# Assigning the results of queries to Python variables (cursor)
cursor = %sql SELECT test_score as "Test Score", count(*) as "Frequency" from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;
cursor

type(cursor)  # sql.run.ResultSet

# Convert cursor to a pandas dataframe
import seaborn
%matplotlib inline

df = cursor.DataFrame()
plot = seaborn.barplot(x='Test Score',y='Frequency', data=df)

# %%Sql Magic configuration
%config SqlMagic

'''
SqlMagic options
--------------
SqlMagic.autocommit=<Bool>
    Current: False
    Set autocommit mode
SqlMagic.autolimit=<Int>
    Current: 0
    Automatically limit the size of the returned result sets
SqlMagic.autopandas=<Bool>
    Current: False
    Return Pandas DataFrames instead of regular result sets
SqlMagic.column_local_vars=<Bool>
    Current: False
    Return data into local variables from column names
SqlMagic.displaylimit=<Int>
    Current: None
    Automatically limit the number of rows displayed (full result set is still stored)
SqlMagic.dsn_filename=<Unicode>
    Current: 'odbc.ini'
    Path to DSN file. When the first argument is of the form [section], a
    sqlalchemy connection string is formed from the matching section in the DSN file.
SqlMagic.feedback=<Bool>
    Current: True
    Print number of rows affected by DML
SqlMagic.short_errors=<Bool>
    Current: True
    Don't display the full traceback on SQL Programming Error
SqlMagic.style=<Unicode>
    Current: 'DEFAULT'
    Set the table printing style to any of prettytable's defined styles
    (currently DEFAULT, MSWORD_FRIENDLY, PLAIN_COLUMNS, RANDOM)
'''

%config SqlMagic.autocommit=False
%config SqlMagic.displaylimit=20
%config SqlMagic.feedback=True

# Close the connection
# Disconnecting programmatically is not possible, halt the notebook instead





"""
More SQL Examples (Practical Use Case)
"""

# Store the dataset in a Table

# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, it
# is highly recommended to manually load the table into the cloud using the database console LOAD tool.
# To proceed, open the Db2 console, open the LOAD tool, select or drag the .CSV file and load the
# dataset into a new table called SCHOOLS. You will need to click on create "(+) New Table" and specify
# the name of the table you want to create and then click "Next".

# Connect to the database
%load_ext sql
%sql ibm_db_sa://cdq34813:1l7vj7-szs45d7qq@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB

# Query the database system catalog to retrieve table metadata
%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA = 'CDQ34813'
%sql select * from SYSCAT.TABLES where TABNAME = 'SCHOOLS'  # verify that table creation was successful

# Query the database system catalog to retrieve column metadata
%sql select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'  # describe the table columns

# How many Elementary Schools are in the dataset?
%sql select count(*) from SCHOOLS where "Elementary, Middle, or High School" = 'ES'

# What is the highest Safety Score?
%sql select MAX("Safety_Score") AS MAX_SAFETY_SCORE from SCHOOLS

# Which schools have highest Safety Score?
%sql select "Name_of_School", "Safety_Score" from SCHOOLS \
    where "Safety_Score" = (select MAX("Safety_Score") from SCHOOLS)

# What are the top 10 schools with the highest "Average Student Attendance"?
%sql select "Name_of_School", "Average_Student_Attendance" from SCHOOLS \
    order by "Average_Student_Attendance" desc nulls last limit 10

# Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance
%sql SELECT "Name_of_School", "Average_Student_Attendance" \
     from SCHOOLS \
     order by "Average_Student_Attendance" \
     fetch first 5 rows only

# Remove the '%' sign from the above result set for Average Student Attendance column
%sql SELECT "Name_of_School", REPLACE("Average_Student_Attendance", '%', '') \
     from SCHOOLS \
     order by "Average_Student_Attendance" \
     fetch first 5 rows only

# Which Schools have Average Student Attendance lower than 70%?
%sql SELECT "Name_of_School", "Average_Student_Attendance" \
     from SCHOOLS \
     where CAST(REPLACE("Average_Student_Attendance", '%', '') AS DOUBLE) < 70 \
     order by "Average_Student_Attendance"

# Get the total College Enrollment (number of students) for each Community Area
%sql select "Community_Area_Name", sum("College_Enrollment__number_of_students_") AS TOTAL_ENROLLMENT \
   from SCHOOLS \
   group by "Community_Area_Name"

# Get the 5 Community Areas with the least total College Enrollment (number of students) sorted in ascending order
%sql select "Community_Area_Name", sum("College_Enrollment__number_of_students_") AS TOTAL_ENROLLMENT \
   from SCHOOLS \
   group by "Community_Area_Name" \
   order by TOTAL_ENROLLMENT asc \
   fetch first 5 rows only
