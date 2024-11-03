# car_rental_system

## Test the different methods in car_rental_system in Postman
To make the connection to Postman, you have to run "python server.py" in your terminal. This will give you a development server. 

## CRUD with customers

### See existing customers in the database
To access the existing customers in the database through Postman, you need the server, and /get_customers, and make sure the method is GET. 
You don't need to write anything to access this information. 
This information will be recieved in JSON-format. 

You can also try to get a customer by name.
To do this you need to change the method from GET to POST, and change to /get_customer_by_name.
Then you need to go to body, change to raw and make sure it is JSON. 
You can try to get Bruce Wayne as your customer.
<img width="644" alt="image" src="https://github.com/user-attachments/assets/a9ede07a-67b2-46f8-99a7-3ce8235894b0">


It should look like this.  

### Create a customer 
To create a customer, you will use the POST method in postman, and change to /save_customer.
You need to add customer_id, name, age and address. 
<img width="626" alt="image" src="https://github.com/user-attachments/assets/a99a7514-663a-4803-b19a-479594d7332e">

Try this to create the customer "Ola Nordmann". 

### Update customer
To update customer, you need to use the PUT method in postman, and change to /update_customer/<customer_id>
You need to write the name, age and address, even if you only want to update one of the values. 
![image](https://github.com/user-attachments/assets/90a09207-034f-4e69-943f-73b327c73f8c)

Try this to update the customer "Ola Nordman", that you just have created. 
You can also use /get_customers to see if the changes you made have been updated in the database. 

### Delete customer
If you want to delete the customer, you need to change to DELETE method in postman, and change to /delete_customer. 
The only parameter you need is the customers name. 
<img width="636" alt="image" src="https://github.com/user-attachments/assets/707ae20d-12ee-40a3-ac53-53956da094e5">

## CRUD with employees

### See existing employees in the database
To see the existing employees in the database, you need to use /get_employees and have the GET method. You will recieve the information on JSON format, and you will get all the employees stored in the database. 

To get access to a specific employee, you need to use /get_employee_by_id and change the method to POST.
It requires the employee_id when you are doing it. 
<img width="635" alt="image" src="https://github.com/user-attachments/assets/f4047918-5790-4d38-9591-1be6ef38b887">

You need to do this to access a specific employee with their employee id. 

### Create an employee
To create an employee, you will use the POST method, and change to /save_employee. 
You need to add employee id, name, address, and branch. 


<img width="640" alt="image" src="https://github.com/user-attachments/assets/1fa56722-7878-4dff-b585-2d35b9fb9e1e">

Make this employee. 

### Update employee
To update the employee, you will use the PUT method, and change to /update_employee/<employee_id>
You need to write the name, address, and branch, even if you only want to change one value. 
![image](https://github.com/user-attachments/assets/622a12c2-5d50-4cde-90c4-9cb6037fc68e)

Try to this to update the employee. To see if the changes you have made has been updated in the database, you can use on of the methods of seeing existing employees in the database. 

### Delete employee
To delete an employee, you will use the DELETE method, and change to /delete_employee. 
You only need the employee id to delete the employee. 
<img width="635" alt="image" src="https://github.com/user-attachments/assets/976813ec-a53c-4939-bbf4-3e45e6d6a269">


## CRUD with cars

### See existing cars in the database
To see the existing cars in the database, you will use the GET method, and change to /get_cars.
With this method you will see all the cars in the database. 

If you only want to find a specific car in the database, you will change to the POST method, and change to /get_cars_by_carid.
Here you need to put in the car id as a parameter. 
<img width="636" alt="image" src="https://github.com/user-attachments/assets/ed7e41c9-ae10-44cb-8edb-bcf88f289874">

Try this, and see if you get the "Mystery Van". 

### Create a car
To create a car in the database, you will use the POST method, and change to /save_car.
You need to add car id, make, model, year, location, and status. 
<img width="637" alt="image" src="https://github.com/user-attachments/assets/0faa70c6-8cda-4a8c-bd7e-9be04ecadd9d">

Try to add this car. 

### Update a car
To update a car in the database, you will use the PUT method, and change to /update_car/<car_id>
You need to write the make, model, year, location, and status, even if you only want to change one value. 

<img width="636" alt="image" src="https://github.com/user-attachments/assets/00a90618-9f43-48fa-bdf2-db80b32a8577">

Try to update the cars status by doing this. 

### Delete a car
To delete a car in the database, you will use the DELETE method, and change to /delete_car
You will only need to write the car id to delete the car. 
<img width="636" alt="image" src="https://github.com/user-attachments/assets/8afe2fc6-8c16-466a-8502-134ebeb5abeb">

Try this to delete the car in the database. 

## Booking and renting cars

### Booking a car
To book a car, you will use the POST method, and change to /order_a_car.
Here you need to write the customers name, and the id for the car you want to book. 
In this scenario you are "Politimester Bastian", and you want to book the BatMobile. 

<img width="632" alt="image" src="https://github.com/user-attachments/assets/f0f473dc-7642-4e12-a5aa-363b30a89e51">

Try this, and see what feedback you gets. 

Unfortunately the Batmobile has already been booked, and "Politimester Bastian" can't book that car. He needs to book a different car, and decides to book "Pelle Politibil". 

"Pelle Politibil" has 3 as the car id. 

<img width="628" alt="image" src="https://github.com/user-attachments/assets/f26417fd-aa56-4356-b44e-d743d8e71034">

### Cancel a booking
To cancel a booking, you will use the POST method, and change to /cancel_car_order. 
Here you need to write the customers name, and the id for the car you want to cancel the booking for. 
In this scenario you are "Bruce Wayne", and you want to cancel the booking you made for the Batmobile (specifically to protect your identity and make sure people don't know you are Batman). 

<img width="632" alt="image" src="https://github.com/user-attachments/assets/c38437cc-08e3-4bf7-af06-0cceceb7398f">

You will need to do this to cancel the booking for the car. 

### Rent a car
To rent a car, you will use the POST method, and change to /rent_car.
Here you need to write the customers name, and the id for the car you want to rent. 
In this scenario you are "Politimester Bastian" again, and this time you want to rent the car "Pelle Politibil". 
It is important that you have booked the car earlier as "Politimester Bastian", and booked the car "Pelle Politibil". 

<img width="635" alt="image" src="https://github.com/user-attachments/assets/e2c5ee3b-f0a7-4f70-b174-a025ea744034">

This is how you rent the car you have previously booked. 

### Return car
To return the car, you will use the POST method, and change to /return_car.
Here you need to write the customers name, the id for the car, and the status of the car when returned. 
In this scenario you are "Politimester Bastian" again, and you want to return the car "Pelle Politibil". 

<img width="635" alt="image" src="https://github.com/user-attachments/assets/ae8fbd13-d8cf-4627-bb41-0f14eb92acdb">

Here you have put the status of the car as "ok", but you can also put the status of the car as "damaged" (depending of how you think "Politimester Bastian" treated the car "Pelle Politibil". 

If the status of the car is put as "ok", the cars status return as "available" in the system, but if the status of the car is "damaged" when returning it, the status of the car will remain as "damaged". 

## Last comments of our system
This is just simple guidelines of how you operate the system using Postman when testing it. You write whatever you like when trying out the different methods, but just remember; keep it pg-13. 













