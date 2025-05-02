import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table
cursor = connection.cursor()

# To drop table if exists
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create table
table_info = """
create table STUDENT(
    NAME VARCHAR(25), CLASS VARCHAR(25), 
    SECTION VARCHAR(25), MARKS INT)
"""
# Execution of query
cursor.execute(table_info)

# Insert some records
cursor.execute("""insert into STUDENT values('Jacob', 'Data Science', 'A', 95)""")
cursor.execute("""insert into STUDENT values('Emily', 'Machine Learning', 'B', 88)""")
cursor.execute("""insert into STUDENT values('Liam', 'Data Science', 'A', 91)""")
cursor.execute("""insert into STUDENT values('Olivia', 'AI & Robotics', 'B', 84)""")
cursor.execute("""insert into STUDENT values('Noah', 'Statistics', 'C', 76)""")
cursor.execute("""insert into STUDENT values('Emma', 'Data Analytics', 'A', 90)""")
cursor.execute("""insert into STUDENT values('Ava', 'Computer Vision', 'B', 85)""")
cursor.execute("""insert into STUDENT values('William', 'Deep Learning', 'A', 93)""")
cursor.execute("""insert into STUDENT values('Sophia', 'NLP', 'B', 87)""")
cursor.execute("""insert into STUDENT values('James', 'Big Data', 'C', 78)""")

# Display all records
print("The executed records are: ")
data = cursor.execute("""select * from STUDENT""")
for i in data:
    print(i) 
    
# Commit changes in the database
connection.commit()
connection.close() 