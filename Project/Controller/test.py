from Project import app
from flask import render_template, request, redirect, url_for, flash
from Project.Model.car import find_car_by_carid, find_all_cars, save_car, update_car, delete_car
from Project.Model.customer import find_customer_by_name, find_all_customers, save_customer, update_customer, delete_customer, customer_booking, customer_rental
from Project.Model.employee import find_employee_by_id, find_all_employees, save_employee, update_employee, delete_employee
import json
# Eg har skifta litt varriabelnamn, så lurt å sjekke i "car", "customer" og "employee" om det er ei endring.


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/get_cars', methods=['GET'])
def query_records():
    return find_all_cars()

@app.route('/get_cars_by_carid', methods=['POST'])
def find_car():
    record = json.loads(request.data)
    print(record)
    print (record['car_id'])
    return find_car_by_carid(record['car_id'])

@app.route('/save_car', methods=['POST'])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record['car_id'], record['make'], record['model'], record['year'], record['location'], record['status'])

@app.route('/update_car', methods=['PUT'])
def update_car_info():
    record = json.loads(request.data)
    return update_car(record['car_id'], record['make'], record['model'], record['year'], record['location'], record['status'])

@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    print (record)
    delete_car(record['car_id'])
    return find_all_cars()

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