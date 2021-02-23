
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://webadmin:CVDggg44341@10.100.2.186:5432/CloudDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

# ##############################begin plane
class planes(db.Model):
    id = db.Column(db.String(13), primary_key=True, unique=True)
    nameplane = db.Column(db.String(50))
    genplane = db.Column(db.String(25))
    
    def __init__(self, id, nameplane, genplane):
        self.id = id
        self.nameplane = nameplane
        self.genplane = genplane


# Create a plane
@app.route('/plane', methods=['POST'])
def add_plane():
    id = request.json['id']
    nameplane = request.json['nameplane']
    genplane = request.json['genplane']

    new_plane = planes(id, nameplane, genplane)

    db.session.add(new_plane)
    db.session.commit()

    return plane_schema.jsonify(new_plane)


# Update a plane
@app.route('/plane/<id>', methods=['PUT'])
def update_plane(id):
    plane = planes.query.get(id)
    
    nameplane = request.json['nameplane']
    genplane = request.json['genplane']

    plane.nameplane = nameplane
    plane.genplane = genplane

    db.session.commit()

    return plane_schema.jsonify(plane)

# Delete plane
@app.route('/plane/<id>', methods=['DELETE'])
def delete_plane(id):
    plane = planes.query.get(id)
    db.session.delete(plane)
    db.session.commit()
    
    return plane_schema.jsonify(plane)

# plane Schema
class planeSchema(ma.Schema):
    class Meta:
        fields =('id', 'nameplane', 'genplane')

# Init Schema 
plane_schema = planeSchema()
planes_schema = planeSchema(many=True)

@app.route('/planes', methods=['GET'])
def get_staffs():
    all_staffs = planes.query.all()
    result1 = planes_schema.dump(all_staffs)
    return jsonify(result1)

# ################################### finish plane
# ##############################begin customer
class customers(db.Model):
    id = db.Column(db.String(10), primary_key=True, unique=True)
    namecustomer = db.Column(db.String(35))
    sex = db.Column(db.String(5))
    
    def __init__(self, id, namecustomer, sex):
        self.id = id
        self.namecustomer = namecustomer
        self.sex = sex


# Create a plane
@app.route('/customer', methods=['POST'])
def add_customer():
    id = request.json['id']
    namecustomer = request.json['namecustomer']
    sex = request.json['sex']

    new_customer = customers(id, namecustomer, sex)

    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)


# Update a customers
@app.route('/customer/<id>', methods=['PUT'])
def update_customer(id):
    customer = customers.query.get(id)
    
    namecustomer = request.json['namecustomer']
    sex = request.json['sex']

    customer.namecustomer = namecustomer
    customer.sex = sex

    db.session.commit()

    return customer_schema.jsonify(customer)

# Delete customers
@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = customers.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    
    return customer_schema.jsonify(customer)

# customer Schema
class customerSchema(ma.Schema):
    class Meta:
        fields =('id', 'namecustomer', 'sex')

# Init Schema 
customer_schema = customerSchema()
customers_schema = customerSchema(many=True)

@app.route('/customers', methods=['GET'])
def get_customers():
    all_customers = customers.query.all()
    result2 = customers_schema.dump(all_customers)
    return jsonify(result2)

# ################################### finish customer


# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    result3 = db.session.query(customers).join(planes)
    return jsonify(result3)

# Run Server
if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=80)