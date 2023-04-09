import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/vicky', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        return jsonify({
            'friends': {
                'name': 'viku',
                'address': 'bombuwala, kalautara-south',
                'educations': {
                    'degree': 'bachelor'
                }   
            }
        })
    elif (request.method == 'POST'):
        return jsonify({
        'city':'kalutara',
        'village':'bombuwala',
        'shops':{
            'sweets':'vimukthi',
            'sports':'sanjaya-shop'
        }
    })

# @app.route('/home', methods=['POST'])
# def home():
#     return jsonify({
#         'city':'kalutara',
#         'village':'bombuwala',
#         'shops':{
#             'sweets':'vimukthi',
#             'sports':'sanjaya-shop'
#         }
#     })
#
# @app.route('/contact', methods=['GET'])
# def contact():
#     return jsonify({
#         'friends':{
#             'name':'viku',
#             'address':'bombuwala, kalautara-south',
#             'educations':{
#                 'degree':'bachelor'
#             }
#         }
#     })

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)