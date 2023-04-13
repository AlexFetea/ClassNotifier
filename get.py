import pymysql
import os

def get_data():
    db = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],\
                         password=os.environ['DB_PASSWORD'],database=os.environ['DB_DATABASE'], port=3306 )

    cursor = db.cursor()

    # Query all CourseNumbers and their LastAccessed values
    cursor.execute("SELECT CourseNumber, LastAccessed FROM Courses;")
    courses_data = cursor.fetchall()

    print(courses_data)

    # Create the dictionary with the desired structure
    courses_dict = {}
    for course_number, last_accessed in courses_data:
        # Get all phone numbers associated with the current course
        cursor.execute(f"SELECT PhoneNumber FROM PhoneNumbers WHERE CourseNumber = '{course_number}';")
        phone_numbers = cursor.fetchall()
        phone_numbers_list = [phone_number[0] for phone_number in phone_numbers]

        # Add the course data to the dictionary
        courses_dict[course_number] = {
            "PhoneNumbers": phone_numbers_list,
            "LastAccessed": last_accessed
        }

    # Close the cursor and the connection
    cursor.close()
    db.close()

    # Print the resulting dictionary
    return courses_dict