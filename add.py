import pymysql
import os

def add(course_num, phone_num):
    db = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],\
                         password=os.environ['DB_PASSWORD'],database=os.environ['DB_DATABASE'], port=3306 )

    cursor = db.cursor()

    query = f'SELECT COUNT(*) FROM Courses WHERE CourseNumber = "{course_num}"'

    cursor.execute(query)

    result = cursor.fetchone()

    if result[0] == 0:
        query = f'INSERT INTO Courses (CourseNumber, LastAccessed) VALUES ("{course_num}", 0.0);'

        cursor.execute(query)

        db.commit()



    query = f'Select COUNT(*) FROM PhoneNumbers WHERE CourseNumber = "{course_num}" && PhoneNumber = "{phone_num}"'

    cursor.execute(query)

    result = cursor.fetchone()

    if result[0] > 0:
        raise Exception('Duplicate Record')

    query = f'INSERT INTO PhoneNumbers (PhoneNumber, CourseNumber) VALUES ("{phone_num}", "{course_num}");'

    cursor.execute(query)

    db.commit()

    db.close()