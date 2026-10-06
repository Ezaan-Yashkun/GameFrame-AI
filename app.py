from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Trained Model Pipeline Load
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Form submission ya API JSON input receive
        data = request.form if request.form else request.get_json()

        gpu_score = float(data.get('gpu_score', 5000))
        cpu_cores = int(data.get('cpu_cores', 6))
        ram_gb = int(data.get('ram_gb', 16))
        resolution = data.get('resolution', '1080p')
        game = data.get('game', 'GTA 5')

        # Input DataFrame prepare
        input_data = pd.DataFrame([[gpu_score, cpu_cores, ram_gb, resolution, game]],
                                  columns=['gpu_score', 'cpu_cores', 'ram_gb', 'resolution', 'game'])

        # FPS Prediction calculate
        predicted_fps = max(5, round(float(model.predict(input_data)[0])))

        # Performance Status Badge generate
        if predicted_fps >= 60:
            status = "Smooth Performance (60+ FPS)"
            badge = "success"
        elif predicted_fps >= 30:
            status = "Playable (30-59 FPS)"
            badge = "warning"
        else:
            status = "Low FPS / Upgrade Needed (<30 FPS)"
            badge = "danger"

        response = {
            'fps': predicted_fps,
            'status': status,
            'badge': badge,
            'game': game,
            'resolution': resolution
        }

        return render_template('index.html', result=response)

    except Exception as e:
        return f"Error occurred: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)