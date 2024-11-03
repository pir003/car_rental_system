from Project import app
from flask import render_template, request, redirect, url_for, flash, jsonify
from Project.Model.car import Car, find_car_by_carid, find_all_cars, save_car, update_car, delete_car
from Project.Model.customer import Customer, find_customer_by_name, find_all_customers, save_customer, update_customer, delete_customer, customer_booking, customer_rental
from Project.Model.employee import Employee, find_employee_by_id, find_all_employees, save_employee, update_employee, delete_employee
from Project.Model.booking import order_car, cancel_car_order, rent_car
import json
# Eg har skifta litt varriabelnamn, så lurt å sjekke i "car", "customer" og "employee" om det er ei endring.


#@app.route('/', methods=["GET", "POST"])
#def index():
#    return render_template("index.html")

@app.route('/get_cars', methods=['GET'])
def query_cars():
    cars = find_all_cars()
    return jsonify(cars)

@app.route('/get_cars_by_carid', methods=['POST'])
def find_car():
    record = request.get_json()
    car = find_car_by_carid(record['car_id'])
    return jsonify(car)

@app.route('/save_car', methods=['POST'])
def save_car_info():
    record = request.get_json()
    save_car(record['car_id'], record['make'], record['model'], record['year'], record['location'], record['status'])
    return jsonify({"message": "Car saved successfully."})

@app.route('/update_car/<car_id>', methods=['PUT']) 
def update_car_info(car_id):
    record = request.get_json()
    update_car(car_id, record['make'], record['model'], record['year'], record['location'], record['status'])
    return jsonify({"message": "Car updated successfully."}) # Same som Sav_cars og Delete

@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = request.get_json()
    delete_car(record['car_id'])
    return jsonify({"message": "Car deleted successfully"}) # Same som Update og save_car

@app.route('/get_customers', methods=['GET'])
def query_cutomers():
    customers = find_all_customers()
    return jsonify(customers)

@app.route('/get_customer_by_name', methods=['POST'])
def find_customer():
    record = request.get_json()
    customer = find_customer_by_name(record['name'])
    return jsonify(customer)

@app.route('/save_customer', methods=['POST'])
def save_customer_info():
    record = request.get_json()
    save_customer(record["customer_id"], record['name'], record['age'], record['address'])
    return jsonify({"message": "Customer saved successfully"})

@app.route('/update_customer/<customer_id>', methods=['PUT']) 
def update_customer_info(customer_id):
    record = request.get_json()
    update_customer(customer_id, record["name"], record['age'], record['address'])
    return jsonify({"message": "Customer updated successfully"})
    
@app.route('/delete_customer', methods=['DELETE'])
def delete_customer_info():
    record = request.get_json()
    delete_customer(record['name'])
    return jsonify({"message": "Customer deleted successfully"})
    
@app.route('/get_employee', methods=['GET'])
def find_employees():
    employees = find_all_employees()
    return jsonify(employees)

@app.route('/get_employee_by_id', methods=['POST'])
def find_employee():
    record = request.get_json()
    employee = find_employee_by_id(record['employee_id'])
    return jsonify(employee)

@app.route('/save_employee', methods=['POST'])
def save_employee_info():
    record = request.get_json()
    save_employee(record['employee_id'], record['name'], record['address'], record['branch'])
    return jsonify({"message": "Employee saved successfully"})

@app.route('/update_employee/<employee_id>', methods=['PUT']) 
def update_employee_info(employee_id):
    record = request.get_json()
    update_employee(employee_id, record['name'], record['address'], record['branch'])
    return jsonify({"message": "Employee updated successfully."})

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee_info():
    record = request.get_json()
    delete_employee(record['employee_id'])
    return jsonify({"message": "Employee deleted successfully."}) # Same som Update og save_car

@app.route('/order_a_car', methods=['POST'])
def order_a_car():
    record = request.get_json()
    result = order_car(record['name'], record['car_id'])
    
    if result.get('success'):
        return jsonify({"message": result['message']})
    else:
        return jsonify({"error": result['error']}), 400

@app.route('/cancel_car_order', methods=['POST'])
def cancel_car():
    record = request.get_json()
    result = cancel_car_order(record['name'], record['car_id'])
    
    if result.get('success'):
        return jsonify({"message": result['message']})
    else:
        return jsonify({"error": result['error']}), 400

@app.route('/rent_car', methods=['POST'])
def rent_a_car():
    record = request.get_json()
    result = rent_car(record['name'], record['car_id'])
    
    if result.get('success'):
        return jsonify({"message": result['message']})
    else:
        return jsonify({"error": result['error']}), 400  

#@app.route('/return_car', methods=['POST'])
#def return_a_car():
    #record = request.get_json()
    #booking = Booking()
    #result = booking.return_car(record['name'], record['car_id'], record['status'])
    
    #if result.get('success'):
        #return jsonify({"message": result['message']})
    #else: 
        #return jsonify({"error": result['error']}), 400

#@app.route('/order_car', methods = ["GET", "POST"])
#def order_car ():
#    if request.method == "POST":
#        customer_id = request.form ["customer_id"]
#        car_id = request.form ["car_id"]

#        if customerBooking(customer_id):
#            flash ("You have already booked a car")
#            return redirect (url_for("..."))
#        
#        car = findCarByCarid(car_id)
#        if car and car.status == "available":
#            updateCar(car_id, status = "booked")
#            flash ("Thank you for booking a car")
#            return redirect (url_for("..."))
#        else:
#            flash ("This car is not available")
#            return redirect (url_for("..."))
#    return render_template ("...")

# cancel_order, rent_car, return_car, add_car, update_car, delete_car, add_customer, update_customer, delete_customer, add_employee, update_employee, delete_employee

#@app.route('/add_car', methods=["GET", "POST"])
#def add_car():
#    if request.method == "POST":
#        make = request.form ["make"]
#        model = request.form ["model"]
#        year = request.form ["year"]
#        location = request.form ["location"]
#        status = request.form ["status"]
    
#        createCar(make, model, year, location, status)
#        return redirect(url_for("..."))
    
#    return render_template ("...")


#    if request.method == "POST":
#        username = request.form["username"]
#        try:
#            user = findUserByUsername(username)
#            data = {
#                "username": user.username,
#                "email": user.email
#            }
#        except err:
#            print (err)

#    else:
#        data = {
#            "username": "Not specified",
#            "email": "Not specified"
#        }
#    return render_template('index.html.j2', data = data)