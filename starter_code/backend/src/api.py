import os
from flask import Flask, request, jsonify, abort
from flask_migrate import Migrate
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import db_drop_and_create_all, setup_db, Drink, db
from auth import AuthError, requires_auth

app = Flask(__name__)

setup_db(app)
migrate = Migrate(app , db)
CORS(app)
with app.app_context():
       db.create_all()

@app.route('/headers')
@requires_auth('get:drinks-detail')
def Hello(jwt):
    print(jwt)
    return 'Hello, Sayed Hussein, the app is working'



'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
#db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['GET'])
#@requires_auth('get:drinks')
def get_drinks():
    drinks_all = Drink.query.all()
    drinks = [drink.short() for drink in drinks_all]
    if len(drinks) == 0:
        abort(404)

    return jsonify({
      'success': True ,
      'drinks' : drinks 
    })
    


  
'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_details(self):
    drinks_all = Drink.query.all()
    print("it works here ")
    print(drinks_all)
    drinks = [drink.long() for drink in drinks_all]
    if len(drinks) == 0:
        abort(404)

    return jsonify({
      'success': True ,
      'drinks' : drinks 
    })


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['post'])
@requires_auth('post:drinks')
def create_new_drink(self):
    body = request.get_json()
    new_title= body.get('title', None)
    new_recipe= body.get('recipe', None)
   
    
    new_drink = Drink(title=new_title , recipe=json.dumps(new_recipe))
    new_drink.insert()
    drinks_all = Drink.query.all()
    drinks = [drink.long() for drink in drinks_all]

    return jsonify ({
        "success": True ,
        "drinks": drinks,     
      })


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt,id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    body = request.get_json()
    drink.title = body.get('title', drink.title)
    drink.recipe = json.dumps(body.get('recipe'))
    drink.update()
    drinks_all = Drink.query.all()
    drinks = [drink.long() for drink in drinks_all]

    return jsonify ({
        "success": True ,
        "drinks": drinks, 
        "modiefed_drink_id" : id
      })


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_specific_drink(jwt,id) :
    selected_drink=Drink.query.get(id)
    selected_drink.delete()
    drinks = Drink.query.all()
    

    if selected_drink is None:
      abort(404)
    
    
    return jsonify ({
        'success': True ,
        'deleted' : id 
      })
    



## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404
'''
@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(400)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 400,
                    "message": "Permission is not included in the JWT"
                    }), 400


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
