from flask import jsonify, request, url_for
from app.api import bp
from app import gol
from app import zoo

z = zoo.Zoo("test")

@bp.route('/v1/lifeforms', methods=['PUT'])
def add_lifeform():
    resp = request.get_json() or {}
    label, cells, width = [resp[k] for k in ('label', 'cells', 'width')]
    
    lf = zoo.Lifeform(label, cells, width)
    z.add(lf)
    response = jsonify(lf.label)
    return response

@bp.route('/v1/lifeforms/<string:label>', methods=['GET'])
def get_lifeform(label):
    lf = z.get(label)

    response = jsonify(lf) 
    response.status_code = 200
    response.headers['Location'] = "v1/lifeforms"
    return response

@bp.route('/v1/lifeforms', methods=['GET'])
def get_lifeforms():
    lf = z.list()

    response = jsonify(lf) 
    response.status_code = 200
    response.headers['Location'] = "v1/lifeforms"
    return response

@bp.route('/v1/lifeforms/<string:label>', methods=['DELETE'])
def delete_lifeform(label):
    lf = z.remove(label)

    response = jsonify(lf) 
    response.status_code = 200
    response.headers['Location'] = "v1/lifeforms"
    return response