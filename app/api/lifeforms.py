from flask import jsonify, request, url_for
from app.api import bp
from app import gol
from app import zoo
from app.api.errors import bad_request

path_to_store = "/Users/tcallahan/Documents/Personal/programming/GameOfLife/app/zoo_storage.txt"
z = zoo.load_zoo(path_to_store)

@bp.route('/v1/lifeforms', methods=['PUT'])
def add_lifeform():
    data = request.get_json() or {}
    if 'label' not in data or 'cells' not in data or 'width' not in data:
        return bad_request('must include label, cells and width in request')
    else:
        label, cells, width = [data[k] for k in ('label', 'cells', 'width')]
    
    lf = zoo.Lifeform(label, cells, width)
    z.add(lf)
    response = jsonify(lf.label)
    response.status_code = 201
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
    lf = z.lst()

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