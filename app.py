from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__)

# Function to create rotation matrix around z-axis
def rotation_matrix_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Function to create translation matrix
def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform():
    data = request.json
    theta = np.radians(data['theta'])
    tx = data['tx']
    ty = data['ty']
    tz = data['tz']
    
    # Create transformation matrix
    transform_matrix = translation_matrix(tx, ty, tz) @ rotation_matrix_z(theta)
    
    return jsonify(transform_matrix.tolist())

if __name__ == '__main__':
    app.run(debug=True)
