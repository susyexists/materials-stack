from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    token = request.cookies.get('token')
    
    # Validate token with SSO
    response = requests.post(
        'https://sso.materials.wiki/auth/validate',
        json={'token': token}
    )
    
    if not response.json().get('valid'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    return jsonify({'data': 'Protected content'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)