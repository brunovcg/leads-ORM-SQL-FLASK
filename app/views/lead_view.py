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

    return jsonify(lead_list), 200


@bp.patch("/lead")
def update():

    return jsonify('ẗeste patch'), 200

@bp.delete("/lead")
def delete_one():

    return jsonify('ẗeste patch'), 200


@bp.get("/")
def welcome():
    return {"Entrega15" : " Leads"}, 200