from Project import app
from flask import render_template, request, redirect, url_for, flash
from Project.Model.car import findCarByCarid, createCar, updateCar, deleteCar
from Project.Model.customer import findCustomerByname, createCustomer, updateCustomer, deleteCustomer, customerBooking, customerRental
from Project.Model.employee import findEmployeeById, createEmployee, updateEmployee, deleteEmployee
#Endrer til storforbokstav, kan være feilen siden Python er case sensitiv og filnavnene våre har stor forbokstav.
#Svar: Eg hadde allereie endra på namna til å ha små bokstavar, men det ser ikkje ut til å ha blitt pusha (og no når eg har endra dei tilbake hjå meg så funkar det, så endringar der blir visst ikkje pusha trur eg)

# Her er det litt feil trur eg, men det ser eg på seinare
#route index
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/order_car', methods = ["GET", "POST"])
def order_car ():
    if request.method == "POST":
        customer_id = request.form ["customer_id"]
        car_id = request.form ["car_id"]

        if customerBooking(customer_id):
            flash ("You have already booked a car")
            return redirect (url_for("..."))
        
        car = findCarByCarid(car_id)
        if car and car.status == "available":
            updateCar(car_id, status = "booked")
            flash ("Thank you for booking a car")
            return redirect (url_for("..."))
        else:
            flash ("This car is not available")
            return redirect (url_for("..."))
    return render_template ("...")

# cancel_order, rent_car, return_car, add_car, update_car, delete_car, add_customer, update_customer, delete_customer, add_employee, update_employee, delete_employee

@app.route('/add_car', methods=["GET", "POST"])
def add_car():
    if request.method == "POST":
        make = request.form ["make"]
        model = request.form ["model"]
        year = request.form ["year"]
        location = request.form ["location"]
        status = request.form ["status"]
    
        createCar(make, model, year, location, status)
        return redirect(url_for("..."))
    
    return render_template ("...")


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