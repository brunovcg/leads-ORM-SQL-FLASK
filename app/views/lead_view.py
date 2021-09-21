from flask import Blueprint, request, current_app, jsonify
from app.models.lead_model import LeadModel


bp = Blueprint("lead", __name__)

@bp.post("/lead")
def create():

    return jsonify('ẗeste post'), 201


@bp.get("/lead")
def create():

    return jsonify('ẗeste get'), 200


@bp.patch("/lead")
def create():

    return jsonify('ẗeste patch'), 200

@bp.delte("/lead")
def create():

    return jsonify('ẗeste patch'), 200





@bp.get("/")
def welcome():
    return {"Entrega15" : " Leads"}, 200