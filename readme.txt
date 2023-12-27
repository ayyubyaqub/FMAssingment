 all the requirements are mentioned in the requirements.txt  file 
 git clone the code from github 

 1)install django 
 2)run command pip install virtualenv
 2.1)virtualenv <envname>
 2.2)<envname>\scripts\activate
 3)activate the virtual environment
 4)pip install -r requirements.txt
 it will install all the dependencies inside the virtual environment



 
 ######################### for signup #################################
 
 method:post:=http://127.0.0.1:8000/api/signup/
 {
    "username":"ayyub123",
    "password":123
}

############################# for login #################################
method:post:=http://127.0.0.1:8000/api/login/
Request:
{
    "username":"ayyub123",
    "password":123
}

Response:
{
    "status": 200,
    "message": "success",
    "data": {
        "username": "ayyub123",
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMzc1NDc1NiwiaWF0IjoxNzAzNjY4MzU2LCJqdGkiOiI4YzdjZGIwNmFlYWY0MTA1OWM1NWNlM2VhYzljMjZiMyIsInVzZXJfaWQiOjN9.ZCjj4El4woG94fRgwPLQnjqBH5N1U67BUin_9r12GN0",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNjY4NjU2LCJpYXQiOjE3MDM2NjgzNTYsImp0aSI6ImNmZTc3NzFjYWNkMTRjNTM5YzBmYzc3ZTA5NGQ0ODg3IiwidXNlcl9pZCI6M30.YuI2N-Iw4Zi9Ix94NfAAZFH9UYwTyDwhcMPoAwR5wfo"
    }
}
now add access key in headers as 
Authorization:'''Bearer +"access"'''


########################################## Vendor #############################3
GET POST http://127.0.0.1:8000/api/vendors/
GET Will return all vendors details

{
    "status": 200,
    "data": [
        {
            "id": 1,
            "name": "kasim shop",
            "contact_details": "963827145",
            "address": "adfreqfds",
            "vendor_code": "FMV2312162009A001",
            "on_time_delivery_rate": 0.0,
            "quality_rating_avg": 6.0,
            "average_response_time": 432.875085,
            "fulfillment_rate": 1.0,
            "created_at": "2023-12-16T14:39:49.338742Z"
        }....
    ]
}

POST will create new instance of vendor
   {
            "name": "kasim shop",
            "contact_details": "963827145",
            "address": "adfreqfds"
        }

        vendor code will be automatically generated
        all these field will be calculated automatically according to the vendor performance
            on_time_delivery_rate
            quality_rating_avg
            average_response_time
            fulfillment_rate

GET http://127.0.0.1:8000/api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/: Delete a vendor.            



################################# Purchase order #####################################


GET POST http://127.0.0.1:8000/api/purchase_orders/
GET WILL Retrieve ALL Purchase order
{
    "status": 200,
    "data": [
        {
            "id": 22,
            "po_number": "FMPO2312261633A002",
            "order_date": "2023-12-26T11:03:39.684611Z",
            "delivery_date": "2023-12-21T09:50:01Z",
            "items": {
                "threads": "157",
                "colour": "black",
                "lenth": "256m"
            },
            "quantity": 65,
            "status": 2,
            "quality_rating": 6.0,
            "issue_date": "2023-12-26T11:03:39.685611Z",
            "acknowledgment_date": "2023-12-26T11:31:26Z",
            "po_delivered_on": "2023-12-26T17:01:31.349101Z",
            "vendor": 1
        },
        {
            "id": 25,
            "po_number": "FMPO2312261702A002",
            "order_date": "2023-12-26T11:32:22.309559Z",
            "delivery_date": null,
            "items": {
                "item": 1
            },
            "quantity": 5,
            "status": 2,
            "quality_rating": null,
            "issue_date": "2023-12-26T11:32:22.309559Z",
            "acknowledgment_date": "2023-12-26T11:33:00Z",
            "po_delivered_on": "2023-12-26T17:23:39.077187Z",
            "vendor": 1
        }
    ]
}



POST will create new instance of Purchase order
    {
            "delivery_date": "2023-12-21T09:50:01Z",
            "items": {
                "threads": "157",
                "colour": "black",
                "lenth": "256m"
            },
            "quantity": 65,
            "issue_date": "2023-12-26T11:03:39.685611Z",
            "vendor": 1
        },

        item should be in json formate
        po_number will autogenerate
        order_date is initiated when purchase order created
        issue_date is initiated when purchase order created
        delivery_date will be assigned to updated
        status is default pending and updated to completed or canceled
        po_delivered_on will be initiated automatically when order is completed 
        vendor is id of vendor instance






● GET http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Delete a purchase order.

request:
● PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Update a purchase order.
         {
            "items": {
                "item": 1,
                "colour":"red"
            },
            "quantity": 5,
            "status": 2,
            "quality_rating": 5.0,
            "vendor": 1
        }

response:
    {
    "status": 201,
    "msg": "Purchase_order updated",
    "data": {
        "id": 27,
        "po_number": "FMPO2312261726A004",
        "order_date": "2023-12-26T11:56:03.521143Z",
        "delivery_date": "2023-12-26T11:55:47Z",
        "items": {
            "item": 1,
            "colour": "red"
        },
        "quantity": 5,
        "status": 2,
        "quality_rating": 5.0,
        "issue_date": "2023-12-26T11:56:03.521143Z",
        "acknowledgment_date": "2023-12-26T11:56:17Z",
        "po_delivered_on": "2023-12-27T15:54:24.482533Z",
        "vendor": 1
    }
}



GET : http://127.0.0.1:8000/api/vendor_performance/vendor_id/
get all performance history vendors by passing vendor id
if vendor id is not passed get all performance history of all vendors



GET /api/vendors/{vendor_id}/performance


{
    "status": 200,
    "data": {
        "id": 1,
        "name": "kasim shop",
        "contact_details": "963827145",
        "address": "adfreqfds",
        "vendor_code": "FMV2312162009A001",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 5.5,
        "average_response_time": 432.875085,
        "fulfillment_rate": 1.0,
        "created_at": "2023-12-16T14:39:49.338742Z"
    }
}


######################################### acknowledge ############################################

POST: http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge
POST REQUEST WITH PURCHASE ORDER ID 
it will update the avarge response time of vendor