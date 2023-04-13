import pymysql
import os

def get_user_courses(phone_num):
    # Connect to the MySQL database
    db = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],\
                         password=os.environ['DB_PASSWORD'],database=os.environ['DB_DATABASE'], port=3306 )

    cursor = db.cursor()

    # Retrieve the CourseNumber values associated with the specified phone number
    cursor.execute(
        "SELECT CourseNumber FROM PhoneNumbers WHERE PhoneNumber = %s;",
        (phone_num,)
    )

    courses = [row[0] for row in cursor.fetchall()]

    # Close the cursor and the connection
    cursor.close()
    db.close()

    # Return the list of associated CourseNumber values
    return courses



