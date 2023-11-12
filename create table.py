from sqlalchemy import create_engine

user ='root'
password = 'password'
host = '127.0.0.1'
port =3306
database ='sham'


def get_connection():
    return  create_engine(
        url="college://{0}:{1}@{2}:{3}/{4}".format(user,password,host,port,database
        )
    )

if __name__ =='__main__':
     try:
        engine=get_connection()
        print(f"connection to the host for user created successfully")
     except Exception as ex:
         print("connection failed\n",ex)
         

        

