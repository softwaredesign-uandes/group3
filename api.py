from flask import Flask, abort, request
import json
from block import Block
from block_model import BlockModel
from api_utils import *

app = Flask(__name__)
block_models = list()


@app.route('/block_models', methods=['GET'])
def get_block_models():
    return json.dumps(dict(block_models=[dict(id=index) for index in range(len(block_models))]))


@app.route('/block_models/<int:block_model_id>', methods=['GET'])
def get_block_model_by_id(block_model_id):
    if block_model_id >= len(block_models):
        abort(404)
    return json.dumps(dict(block_model=dict(
        id=block_model_id,
        total_weigth=block_models[block_model_id].total_weight(),
        num_blocks=block_models[block_model_id].num_blocks(),
        air_blocks_percentage=0,
        mineral_weight=block_models[block_model_id].mineral_weight()
    )))


@app.route('/block_models', methods=['POST'])
def create_block_model():
    data = request.get_json()['block_model']
    coordinates = build_model_coordinates(data)
    weights = data['weights']
    grades = data['grades']
    mineral_names = grades.keys()
    minerals = list(zip([grades[mineral_name] for mineral_name in mineral_names]))

    blocks = list(map(
        lambda item: Block(
            item[1][0],
            item[1][1],
            item[1][2],
            weights[item[0]],
            get_block_minerals(minerals, mineral_names, item[0])
        ),
        enumerate(coordinates)
    ))
    block_model = BlockModel()
    block_model.replace_blocks(blocks)
    block_models.append(block_model)

    return json.dumps(dict(id=len(block_models)-1))


@app.route('/block_models/<int:block_model_id>/blocks', methods=['GET'])
def get_block_model_blocks(block_model_id):
    if block_model_id >= len(block_models):
        abort(404)
    return json.dumps(
        dict(
            blocks=list(map(
                lambda block: block.__dict__,
                block_models[block_model_id].blocks
            ))
        )
    )


@app.route('/block_models/<int:block_model_id>/blocks/<int:block_id>', methods=['GET'])
def get_block_model_block(block_model_id, block_id):
    if block_model_id >= len(block_models):
        abort(404)
    block = block_models[block_model_id].get_block_by_id(block_id)
    if block is None:
        abort(404)
    return json.dumps(
        dict(
            block=block.__dict__
        )
    )