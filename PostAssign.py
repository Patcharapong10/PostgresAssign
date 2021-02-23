
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
    result = planes_schema.dump(all_staffs)
    return jsonify(result)

# ################################### finish 

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud Patcharapong'})

# Run Server
if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=80)