import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres",user="postgres" ,password="123@Omjite",host="localhost",port="5433") 

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int) ''')

    print('Created Successfully')

    conn.commit()
    conn.close()
def data():
    conn = psycopg2.connect(dbname="postgres",user="postgres" ,password="123@Omjite",host="localhost",port="5433") 
    cursor = conn.cursor()
    
    name = input('Enter name: ')
    id = input('Enter id: ')
    age = input('Enter age: ')

    query = '''insert into employees(Name, ID, Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))


    print('Added Successfully')

    conn.commit()
    conn.close()
    
data()
