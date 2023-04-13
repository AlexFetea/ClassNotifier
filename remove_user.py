import pymysql
import os

def remove_user(course_num, phone_num):
    db = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],\
                         password=os.environ['DB_PASSWORD'],database=os.environ['DB_DATABASE'], port=3306 )

    cursor = db.cursor()

    query = f'SELECT COUNT(*) FROM PhoneNumbers WHERE CourseNumber = "{course_num}" AND PhoneNumber = "{phone_num}"'

    cursor.execute(query)

    result = cursor.fetchone()

    if result[0] == 0:
        raise Exception('Record does not exist')

    # Remove the specified phone number and course number pairing from the PhoneNumbers table
    cursor.execute(
        "DELETE FROM PhoneNumbers WHERE PhoneNumber = %s AND CourseNumber = %s;",
        (phone_num, course_num)
    )

    # Check if there are any remaining phone numbers associated with the course number
    cursor.execute(
        "SELECT COUNT(*) FROM PhoneNumbers WHERE CourseNumber = %s;",
        (course_num,)
    )
    remaining_phone_numbers_count = cursor.fetchone()[0]

    # If there are no remaining phone numbers, remove the course from the Courses table
    if remaining_phone_numbers_count == 0:
        cursor.execute(
            "DELETE FROM Courses WHERE CourseNumber = %s;",
            (course_num,)
        )

    # Commit the changes and close the cursor and the connection
    db.commit()
    cursor.close()
    db.close()