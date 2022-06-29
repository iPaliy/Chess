from flask import Flask
from flask_restful import Api, Resource
from chess import *

app = Flask(__name__)
api = Api()

available_moves = {
    "availableMoves": None,
    "error": None,
    "figure": None,
    "currentField": None
}

valid_moves = {
    "move": '',
    "figure": None,
    "error": '',
    "currentField": None,
    "destField": None

}


class All(Resource):
    @staticmethod
    def get(figur, current_field):
        if figur == 'king':
            King.turn(current_field)
            available_moves["availableMoves"] = Figure.list_turn
            available_moves["error"] = Figure.error
            available_moves["figure"] = Figure.figur_name
            available_moves["currentField"] = Figure.current_field
            return available_moves
        elif figur == 'queen':
            Queen.turn(current_field)
            available_moves["availableMoves"] = Figure.list_turn
            available_moves["error"] = Figure.error
            available_moves["figure"] = Figure.figur_name
            available_moves["currentField"] = Figure.current_field
            return available_moves
        elif figur == 'rook':
            Rook.turn(current_field)
            available_moves["availableMoves"] = Figure.list_turn
            available_moves["error"] = Figure.error
            available_moves["figure"] = Figure.figur_name
            available_moves["currentField"] = Figure.current_field
            return available_moves
        elif figur == 'bishops':
            Bishops.turn(current_field)
            available_moves["availableMoves"] = Figure.list_turn
            available_moves["error"] = Figure.error
            available_moves["figure"] = Figure.figur_name
            available_moves["currentField"] = Figure.current_field
            return available_moves
        elif figur == 'knights':
            Knights.turn(current_field)
            available_moves["availableMoves"] = Figure.list_turn
            available_moves["error"] = Figure.error
            available_moves["figure"] = Figure.figur_name
            available_moves["currentField"] = Figure.current_field
            return available_moves
        elif figur == 'pawns':
            Pawns.turn(str(current_field))
            available_moves["availableMoves"] = Figure.list_turn
            available_moves["error"] = Figure.error
            available_moves["figure"] = Figure.figur_name
            available_moves["currentField"] = Figure.current_field
            return available_moves


class Valid(Resource):
    @staticmethod
    def get(figur, current_field, dest_field):
        if figur == 'king':
            King.turn(current_field)
            if dest_field.upper() in Figure.list_turn:
                valid_moves["move"] = 'Valid'
                valid_moves["error"] = None
            else:
                valid_moves["move"] = 'Invalid'
                valid_moves["error"] = 'Current move is not permitted.'
            valid_moves["figure"] = Figure.figur_name
            valid_moves["currentField"] = Figure.current_field
            valid_moves["destField"] = dest_field.upper()
            return valid_moves

        elif figur == 'queen':
            Queen.turn(current_field)
            if dest_field.upper() in Figure.list_turn:
                valid_moves["move"] = 'Valid'
                valid_moves["error"] = None
            else:
                valid_moves["move"] = 'Invalid'
                valid_moves["error"] = 'Current move is not permitted.'
            valid_moves["figure"] = Figure.figur_name
            valid_moves["currentField"] = Figure.current_field
            valid_moves["destField"] = dest_field.upper()
            return valid_moves

        elif figur == 'rook':
            Rook.turn(current_field)
            if dest_field.upper() in Figure.list_turn:
                valid_moves["move"] = 'Valid'
                valid_moves["error"] = None
            else:
                valid_moves["move"] = 'Invalid'
                valid_moves["error"] = 'Current move is not permitted.'
            valid_moves["figure"] = Figure.figur_name
            valid_moves["currentField"] = Figure.current_field
            valid_moves["destField"] = dest_field.upper()
            return valid_moves

        elif figur == 'bishops':
            Bishops.turn(current_field)
            if dest_field.upper() in Figure.list_turn:
                valid_moves["move"] = 'Valid'
                valid_moves["error"] = None
            else:
                valid_moves["move"] = 'Invalid'
                valid_moves["error"] = 'Current move is not permitted.'
            valid_moves["figure"] = Figure.figur_name
            valid_moves["currentField"] = Figure.current_field
            valid_moves["destField"] = dest_field.upper()
            return valid_moves

        elif figur == 'knights':
            Knights.turn(current_field)
            if dest_field.upper() in Figure.list_turn:
                valid_moves["move"] = 'Valid'
                valid_moves["error"] = None
            else:
                valid_moves["move"] = 'Invalid'
                valid_moves["error"] = 'Current move is not permitted.'
            valid_moves["figure"] = Figure.figur_name
            valid_moves["currentField"] = Figure.current_field
            valid_moves["destField"] = dest_field.upper()
            return valid_moves

        elif figur == 'pawns':
            Pawns.turn(str(current_field))
            if dest_field.upper() in Figure.list_turn:
                valid_moves["move"] = 'Valid'
                valid_moves["error"] = None
            else:
                valid_moves["move"] = 'Invalid'
                valid_moves["error"] = 'Current move is not permitted.'
            valid_moves["figure"] = Figure.figur_name
            valid_moves["currentField"] = Figure.current_field
            valid_moves["destField"] = dest_field.upper()
            return valid_moves


api.add_resource(All, '/api/v1/<figur>/<current_field>/')
api.add_resource(Valid, '/api/v1/<figur>/<current_field>/<dest_field>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
