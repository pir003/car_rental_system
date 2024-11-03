# car_rental_system

# Test the different methods in car_rental_system in Postman
To make the connection to Postman, you have to run "python server.py" in your terminal. This will give you a development server. 

# See existing customers in the database
To access the existing customers in the database through Postman, you need the server, and /get_customers, and make sure the method is GET. 
You don't need to write anything to access this information. 
This information will be recieved in JSON-format. 

You can also try to get a customer by name.
To do this you need to change the method from GET to POST, and change to /get_customer_by_name.
Then you need to go to body, change to raw and make sure it is JSON. 
You can try to get Bruce Wayne as your customer.
<img width="644" alt="image" src="https://github.com/user-attachments/assets/a9ede07a-67b2-46f8-99a7-3ce8235894b0">


It should look like this.  

# Create a customer 
To create a customer, you will use the POST method in postman, and change to /save_customer.
You need to add customer_id, name, age and address. 
<img width="626" alt="image" src="https://github.com/user-attachments/assets/a99a7514-663a-4803-b19a-479594d7332e">

Try this to create the customer "Ola Nordmann". 

# Delete customer
If you want to delete the customer, you need to change to DELETE method in postman, and change to /delete_customer. 
The only parameter you need is the customers name. 
<img width="636" alt="image" src="https://github.com/user-attachments/assets/707ae20d-12ee-40a3-ac53-53956da094e5">



