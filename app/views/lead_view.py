from flask import Blueprint, request, current_app, jsonify
from app.models.lead_model import LeadModel
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc


bp = Blueprint("lead", __name__)

@bp.post("/lead")
def create():

    data = request.get_json()

    new_entry = LeadModel(
        name=data["name"],
        email = data["email"],
        phone = data["phone"],
        creation_date = datetime.today(),
        last_visit = datetime.today(),
        visits = 1
    )
   
    if not LeadModel.isPhoneFormated(data["phone"]):
        return {"Error" : "Phone must have '(xx)xxxxx-xxxx' format"}, 400
  
    try:
        session = current_app.db.session
        session.add(new_entry)
        session.commit()

    except IntegrityError:
        return {"Error" : "E-mail or Phone already exists"}, 409

    return jsonify(new_entry), 201


@bp.get("/lead")
def get_all():

    query = LeadModel.query.order_by(desc('visits'))

    lead_list = [
            {"id": card.id, "name": card.name, "name": card.name,
             "email" : card.email, "phone" : card.phone, 
             "creation_date" : card.creation_date, "last_visit" : card.last_visit,
             "visits" : card.visits
             }
            for card in query
    ]

    if lead_list == []:
        return {"Error" : "No data in DATABASE"}, 404

    return jsonify(lead_list), 200


@bp.patch("/lead")
def update():

    data = request.get_json()

    try:
        data["email"]
        if len(data) != 1:
            return {"error" : "there more entries than necessary, you only need 'email' in request"}, 400
    except KeyError:
        return {"error" : "there is no 'email' in request"}, 400


    if type(data['email']) != str:
        return {"Error" : "Email must be a String"}, 400

    checkDatabaseEmpty = LeadModel.query.all()

    if checkDatabaseEmpty  == []:
        return {"Error" : "No data in DATABASE"}, 404


    lead = LeadModel()

    query = lead.query.filter_by(email = data['email']).first()

    if not query:
        return {"error" : "this email is not in DATABASE"}, 404


    new_data = {"visits" : (query.visits + 1), "last_visit" : datetime.today()}

    for key, value in new_data.items():
        setattr(query, key, value)

    current_app.db.session.add(query)
    current_app.db.session.commit()

    return "", 200



@bp.delete("/lead")
def delete_one():

    data = request.get_json()

    try:
        data["email"]
        if len(data) != 1:
            return {"error" : "there more entries than necessary, you only need 'email' in request"}, 400
    except KeyError:
        return {"error" : "there is no 'email' in request"}, 400


    if type(data['email']) != str:
        return {"Error" : "Email must be a String"}, 400

    checkDatabaseEmpty = LeadModel.query.all()

    if checkDatabaseEmpty  == []:
        return {"Error" : "No data in DATABASE"}, 404

    lead = LeadModel()

    query = lead.query.filter_by(email = data['email']).first()

    if not query:
        return {"error" : "this email is not in DATABASE"}, 404


    current_app.db.session.delete(query)
    current_app.db.session.commit()


    return "", 204


@bp.get("/")
def welcome():
    return {"Entrega15" : " Leads"}, 200