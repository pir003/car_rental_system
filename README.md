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
Write:
{
    "name": "Bruce Wayne"
}