from Project import app
from flask import render_template, request, redirect, url_for, flash
from Project.Model.car import Car, find_car_by_carid, find_all_cars, save_car, update_car, delete_car
from Project.Model.customer import Customer, find_customer_by_name, find_all_customers, save_customer, update_customer, delete_customer, customer_booking, customer_rental
from Project.Model.employee import Employee, find_employee_by_id, find_all_employees, save_employee, update_employee, delete_employee
from Project.Model.booking import Booking
import json
# Eg har skifta litt varriabelnamn, så lurt å sjekke i "car", "customer" og "employee" om det er ei endring.


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/get_cars', methods=['GET'])
def query_cars():
    cars = find_all_cars()
    return render_template("cars.html", cars = cars)

@app.route('/get_cars_by_carid', methods=['POST'])
def find_car():
    record = json.loads(request.data)
    json.dumps(find_car_by_carid(record['car_id']))
    return render_template("cars.html", record['car_id'])

@app.route('/save_car', methods=['GET', 'POST'])
def save_car_info():
    if request.method == 'POST':
        record = json.loads(request.data)
        save_car(record['car_id'], record['make'], record['model'], record['year'], record['location'], record['status'])
        flash("Car saved successfully.", "success")
        return redirect(url_for("query_cars")) # Same som Delet og Update
    return render_template("save_or_edit_cars.html")

@app.route('/update_car', methods=['PUT']) 
def update_car_info(car_id):
    record = json.loads(request.data)
    update_car(record['car_id'], record['make'], record['model'], record['year'], record['location'], record['status'])
    flash("Car updated successfully.", "success")
    return render_template("save_or_edit_cars.html") # Same som Sav_cars og Delete

@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    delete_car(record['car_id'])
    flash("Car deleted successfully.", "success")
    return redirect(url_for("query_cars")) # Same som Update og save_car

@app.route('/get_customers', methods=['GET'])
def query_cutomers():
    customers = find_all_customers()
    return render_template("customer.html", customers = customers)

@app.route('/get_customer_by_name', methods=['POST'])
def find_customer():
    record = json.loads(request.data)
    json.dumps(find_customer_by_name(record['name']))
    return render_template("customer.html", record['name'])

@app.route('/save_customer', methods=['GET', 'POST'])
def save_customer_info():
    if request.method == 'POST':
        record = json.loads(request.data)
        save_car(record['name'], record['age'], record['address'])
        flash("Customer saved successfully.", "success")
        return redirect(url_for("customer_query")) # Same som Delet og Update
    return render_template("save_or_edit_customer.html")

@app.route('/update_customer', methods=['PUT']) 
def update_customer_info():
    record = json.loads(request.data)
    update_car(record['name'], record['age'], record['address'])
    flash("Customer updated successfully.", "success")
    return render_template("save_or_edit_customers.html") # Same som Sav_cars og Delete

@app.route('/delete_customer', methods=['DELETE'])
def delete_customer_info():
    record = json.loads(request.data)
    delete_car(record['name'])
    flash("Customer deleted successfully.", "success")
    return redirect(url_for("query_customers")) # Same som Update og save_car

@app.route('/get_employee', methods=['GET'])
def query_employee():
    employees = find_all_employees()
    return render_template("employees.html", employees = employees)

@app.route('/get_employee_by_id', methods=['POST'])
def find_employee():
    record = json.loads(request.data)
    json.dumps(find_employee_by_id(record['employee_id']))
    return render_template("employess.html", record['employee_id'])

@app.route('/save_employee', methods=['GET', 'POST'])
def save_employee_info():
    if request.method == 'POST':
        record = json.loads(request.data)
        save_employee(record['employee_id'], record['name'], record['address'], record['branch'])
        flash("Employee saved successfully.", "success")
        return redirect(url_for("query_employees")) # Same som Delet og Update
    render_template("save_or_edit_employee.htmls")

@app.route('/update_employee', methods=['PUT']) 
def update_emplyee_info():
    record = json.loads(request.data)
    update_employee(record['employee_id'], record['name'], record['address'], record['branch'])
    flash("Employee updated successfully.", "success")
    return render_template("save_or_edit_employees.html") # Same som Sav_cars og Delete

@app.route('/delete_customer', methods=['DELETE'])
def delete_employee_info():
    record = json.loads(request.data)
    delete_employee(record['employee_id'])
    flash("Employee deleted successfully.", "success")
    return redirect(url_for("query_employees")) # Same som Update og save_car

@app.route('/order_a_car', methods=['GET','POST'])
def order_a_car():
    if request.method == 'POST':
        name = request.form['name']
        car_id = request.form['car_id']
        booking = Booking()
        result = booking.order_car(name, car_id)

        if result.get('success'):
            flash(result['message'], 'success')
            return redirect (url_for("..."))
        else:
            flash(result['error'], 'error')
    
        return redirect(url_for("query_cars"))

@app.route('/cancel_car_order', methods=['POST'])
def cancel_car():
    name = request.form['name']
    car_id = request.form['car_id']
    booking = Booking()
    result = booking.cancel_car_order(name, car_id)

    if result.get('success'):
        flash(result['message'], 'success')
        return redirect (url_for("..."))
    else:
        flash(result['error'], 'error')
    
    return redirect(url_for("query_cars"))

@app.route('/rent_car', methods=['POST'])
def rent_a_car():
    name = request.form['name']
    car_id = request.form['car_id']
    booking = Booking()
    result = booking.rent_car(name, car_id)

    if result.get('success'):
        flash(result['message'], 'success')
        return redirect (url_for("..."))
    else:
        flash(result['error'], 'error')
    
    return redirect(url_for("query_cars"))

@app.route('/return_car', methods=['POST'])
def return_a_car():
    name = request.form['name']
    car_id = request.form['car_id']
    status = request.form['status']
    booking = Booking()
    result = booking.return_car(name, car_id, status)

    if result.get('success'):
        flash(result['message'], 'success')
        return redirect (url_for("..."))
    else:
        flash(result['error'], 'error')
    
    return redirect(url_for("query_cars"))

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