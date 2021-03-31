REQUIRES PYTHON 3.7!

To install the server run install.CMD

Than to run the server use RUN.CDM


for development only:

How to interact with the API:

Every api call which will result in a change in de DB will need a JWT token

How to get the JWT token:
send a post request to localhost:5000/login
with the following JSON body:
{
	"email" : "admin_email_address",
	"password" : "admin_password"
}

In response you will get a JWT token like:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDIyNzI5NjYsIm5iZiI6MTYwMjI3Mjk2NiwianRpIjoiZDgyNmM2YWMtMDRjNC00ZjNiLWE4OWUtNDAwMGMwMmI2ZGRlIiwiZXhwIjoxNjAyMjczODY2LCJpZGVudGl0eSI6ImFkbWluX2VtYWlsX2FkZHJlc3MiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.QmTdvtRH01rZ1r7HbMzW-XPJPjwtYuwiRj43nuh4xu8"

Send this token in the header(autorisation) with Bearer <token> to get access to all api calls

___________________________________________________________________________________________________________

JSON formats:
"/add_blog" POST (use token)
Use this call to add a blog to the database
{
	"title" : "",
	"content" : "",
	"feature_image" : "",
	"tags" : [""]
}

"/blogs" GET (dont need token)
Use this call to get all blogs from the database
{
    "all_blogs": [
        {
            "content": "",
            "creation_date": "",
            "feature_image": "",
            "id": ,
            "title": ""
        },
        {
            "content": "",
            "creation_date": "",
            "feature_image": "",
            "id": ,
            "title": ""
        },
}

User can login by sending a json in the following structure POST to the /login page
{
	"email" : "",
	"password" : ""
}

if the log in is correct the following response will be recieved:

{
    "email": "",
    "role": ""
}

role can be 0,1,2
0 = system admin
1 = admin
2 = user

for test use: 
admin=User(email="admin_email_address",password="admin_password",role=0) returns the JWT Token
admin2=User(email="Test_Admin",password="123123",role=1)
admin3=User(email="Test_User",password="123123",role=2)

to add a user send the following to POST /adduser:
{
	"email" : "",
	"password" : "",
}

A user can save his favorite tags on his profile. add a tag to store to a users profile; 


Send this to /upimages to upload a image
{ "file_name" : "", "file_data" : "" }

use /getallimg to get all images paths

use:
set FLASK_APP=api 
flash run
