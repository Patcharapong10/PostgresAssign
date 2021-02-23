
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






# Staff Schema
class StaffSchema(ma.Schema):
    class Meta:
        fields =('id', 'nameplane', 'genplane')

# Init Schema 
staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud Patcharapong'})

@app.route('/planes', methods=['GET'])
def get_staffs():
    all_staffs = planes.query.all()
    result = staffs_schema.dump(all_staffs)
    return jsonify(result)


# Run Server
if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0.0', port=80)