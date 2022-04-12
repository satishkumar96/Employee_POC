import database_connection


def lambda_handler(event, context):
    conn = database_connection.database()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Emp_Id, First_Name, Last_name, Designation "
                           "FROM Emp_Details"
                           )
            result = cursor.fetchall()
            conn.commit()

            def get_id(id):
                cursor.execute("SELECT Qualification, Marks "
                               "FROM Emp_Education "
                               "WHERE Emp_Id = %s", id)

                edu_result = cursor.fetchall()
                conn.commit()

                data = []
                for j in range(0, len(edu_result)):
                    data.append(
                        {
                            "course": edu_result[j]["Qualification"],
                            "marks": edu_result[j]["Marks"]
                        }
                    )
                return data

            def get_result(emp_id, f_name, l_name, desi):
                my_dict = {
                    "id": emp_id,
                    "firstName": f_name,
                    "lastName": l_name,
                    "designation": desi,
                    "qualification": (get_id(emp_id))
                }

                return my_dict

            data = []
            for i in range(0, len(result)):
                data.append(get_result \
                        (
                        result[i]["Emp_Id"],
                        result[i]["First_Name"],
                        result[i]["Last_name"],
                        result[i]["Designation"]
                    )
                )

            return data

    finally:
        conn.close()
