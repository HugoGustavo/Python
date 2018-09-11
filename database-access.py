import psycopg2;

connection = psycopg2.connect(host='localhost', database='TEST', user='postgres', password='root');
cursor = connection.cursor();
sql = """
    create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float
    )
""";

#cursor.execute(sql);
connection.commit();
connection.close();

connection = psycopg2.connect(host='localhost', database='TEST', user='postgres', password='root');
cursor = connection.cursor();
sql = """
    insert into employee(first_name, last_name, age, sex, income) values('Mac', 'Mohan', 20, 'M', 2000)
""";
try:
    cursor.execute(sql);
    connection.commit();
except:
    connection.rollback();
connection.close();

connection = psycopg2.connect(host='localhost', database='TEST', user='postgres', password='root');
cursor = connection.cursor()
sql = "select * from employee where income > '%d' " % (1000);
try:
    cursor.execute(sql);
    results = cursor.fetchall();

    for row in results:
        register = {};
        register['fname']=row[0];
        register['lname']=row[1];
        register['age']=row[2];
        register['sex']=row[3];
        register['income']=row[4];
        print(register);
except:
    print("Error: unable to fetch data");

connection.close();

connection = psycopg2.connect(host='localhost', database='TEST', user='postgres', password='root');
cursor = connection.cursor();
sql = "delete from employee where age >= 20";
try:
    #cursor.execute(sql);
    connection.commit();
except:
    print("error");
    connection.rollback();
connection.close();