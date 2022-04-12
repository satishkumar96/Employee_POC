import pymysql.cursors

Endpoint = 'aws-simple.cailsq3lbmea.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'adminroot1234'
database_name = 'Employee'


def database():
    conn = pymysql.connect(host=Endpoint,
                           user=username,
                           password=password,
                           database=database_name,
                           cursorclass=pymysql.cursors.DictCursor
                           )
    return conn
