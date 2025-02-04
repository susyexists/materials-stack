from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
SECRET_KEY = "your-sso-secret-key"  # Replace with a secure key

# Mock user database
users = {
    "user@materials.wiki": {"password": "securepassword"}
}

@app.route('/auth/token', methods=['POST'])
def create_token():
    data = request.json
    user = users.get(data.get('email'))
    
    if user and user['password'] == data.get('password'):
        token = jwt.encode({
            'sub': data['email'],
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({"access_token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/auth/validate', methods=['POST'])
def validate_token():
    token = request.json.get('token')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({"valid": True, "sub": payload['sub']})
    except jwt.ExpiredSignatureError:
        return jsonify({"valid": False, "error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"valid": False, "error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)