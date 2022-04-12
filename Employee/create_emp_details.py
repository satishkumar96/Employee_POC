import pymysql.err

import database_connection


def lambda_handler(event, context):
    conn = database_connection.database()

    try:
        with conn.cursor() as cursor:
            First_Name = event['firstName']
            Last_Name = event['lastName']
            Designation = event['designation']


            """Insert Employee Details in Emp_Details Table"""
            insert_sql = "insert into Emp_Details(First_Name, Last_Name, Designation) values" \
                         "(%s, %s, %s)"
            cursor.execute(insert_sql, (First_Name, Last_Name, Designation))
            conn.commit()

            """Get Latest Added Employee ID from Emp_Details Table"""
            cursor.execute("SELECT Emp_Id FROM Emp_Details ORDER BY Emp_Id  DESC LIMIT 1")
            emp_id = cursor.fetchall()
            conn.commit()

            """Insert Employee Education Details in Emp_Education Table"""
            for i in range(0, len(event["qualification"])):
                cursor.execute("INSERT INTO Emp_Education() VALUES "
                               "(%s, %s, %s)", (emp_id[0]['Emp_Id'], event["qualification"][i]["course"], event["qualification"][i]["marks"]))
                conn.commit()

            success_response = [{"message": "Employee Added Successfully"}]

            return success_response

    finally:
        conn.close()
