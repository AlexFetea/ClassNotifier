import pymysql
import time
import os

def update_last_accessed(course_num):
        # Connect to the MySQL database
        db = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],\
                        password=os.environ['DB_PASSWORD'],database=os.environ['DB_DATABASE'], port=3306 )

        cursor = db.cursor()

        # Get the current UNIX timestamp
        current_timestamp = time.time()

        # Update the LastAccessed value for the given course number
        cursor.execute(
            "UPDATE Courses SET LastAccessed = %s WHERE CourseNumber = %s;",
            (current_timestamp, course_num)
        )

        # Commit the changes and close the cursor and the connection
        db.commit()
        cursor.close()
        db.close()