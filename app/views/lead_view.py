from flask import Blueprint, request, current_app, jsonify
from app.models.lead_model import LeadModel


bp = Blueprint("lead", __name__)

@bp.post("/lead")
def create():

    return jsonify('ẗeste post'), 201


@bp.get("/lead")
def get_all():

    return jsonify('ẗeste get'), 200


@bp.patch("/lead")
def update():

    return jsonify('ẗeste patch'), 200

@bp.delete("/lead")
def delete_one():

    return jsonify('ẗeste patch'), 200


@bp.get("/")
def welcome():
    return {"Entrega15" : " Leads"}, 200