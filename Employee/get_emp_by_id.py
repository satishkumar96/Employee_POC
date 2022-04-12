import database_connection


def lambda_handler(event, context):
    conn = database_connection.database()

    try:
        with conn.cursor() as cursor:
            Emp_id = event['Emp_id']
            cursor.execute("SELECT d.Emp_Id, d.First_Name, d.Last_name, d.Designation, e.Qualification, e.Marks "
                           "FROM Emp_Details as d "
                           "JOIN Emp_Education as e on d.Emp_Id = e.Emp_Id "
                           "WHERE d.Emp_Id = %s", Emp_id)
            result = cursor.fetchall()
            conn.commit()

            if not result:
                failure_response = [{"message": "Employee ID not Exists"}]

                return failure_response
            else:

                def get_result():
                    get_qual = []
                    for i in range(0, len(result)):
                        get_qual.append(
                            {
                                "course": result[i]["Qualification"],
                                "marks": result[i]["Marks"]
                            }
                        )

                    return get_qual

                data = [{
                    "id": result[0]["Emp_Id"],
                    "firstName": result[0]["First_Name"],
                    "lastName": result[0]["Last_name"],
                    "designation": result[0]["Designation"],
                    'qualifications': (get_result())
                }]
                return data

    finally:
        conn.close()
