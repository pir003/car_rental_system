from project import app
from flask import render_template, request, redirect, url_for
from project.model.car import findCarByCarid, createCar, updateCar, deleteCar
from project.model.customer import findCustomerByname, createCustomer, updateCustomer, deleteCustomer
from project.model.employee import findEmployeeById, createEmployee, updateEmployee, deleteEmployee


#route index
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

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