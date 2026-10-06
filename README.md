# 🎮 GameFrame AI - Smart FPS & Hardware Benchmark Predictor

**GameFrame AI** is a Machine Learning-powered web application that predicts frame rate (FPS) performance and estimates hardware capability for modern PC gaming titles. Designed to bridge hardware benchmarking and machine learning regression models, GameFrame AI helps gamers and PC builders evaluate performance bottlenecks before buying hardware or running games.

## ✨ Features

* ⚡ **Machine Learning FPS Estimation:** Powered by a trained **Random Forest Regressor** pipeline.

* 🎯 **Categorical Preprocessing:** Uses `ColumnTransformer` and `OneHotEncoder` to handle non-numeric inputs like game titles and display resolutions seamlessly.

* 🖥️ **Hardware Benchmark Inputs:** Accepts GPU benchmark scores, CPU core counts, system RAM, target resolution, and game selection.

* 🚦 **Dynamic Performance Status:** Categorizes results into **Smooth (60+ FPS)**, **Playable (30-59 FPS)**, and **Low FPS (<30 FPS)** badge indicators.

* 🌌 **Futuristic Dark Dashboard:** Built using custom Bootstrap 5 styling with neon gaming accents for a modern user interface.

## 🛠️ Tech Stack

* **Core Engine:** Python 3.10+

* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib

* **Web Backend:** Flask

* **Frontend UI:** HTML5, CSS3, Bootstrap 5

## 📂 Project Architecture

```
GameFrame_AI/
├── dataset/
│   └── benchmark_data.csv   # Game performance & hardware metrics dataset
├── templates/
│   └── index.html           # Dark-themed gaming dashboard UI
├── train.py                 # Scikit-learn ML pipeline training script
├── app.py                   # Flask server and inference routing
├── model.pkl                # Exported trained Random Forest pipeline
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

```

## 🚀 Quickstart & Setup

### 1. Clone the Repository

```
git clone https://github.com/Ezaan-Yashkun/GameFrame-AI.git
cd GameFrame-AI

```

### 2. Set Up Virtual Environment

```
python -m venv .venv
# On Windows PowerShell:
.venv\Scripts\activate

```

### 3. Install Dependencies

```
pip install -r requirements.txt

```

### 4. Train the ML Model

```
python train.py

```

### 5. Launch the Application

```
python app.py

```

Open `http://127.0.0.1:5000` in your web browser to test predictions.

## 📊 Dataset Parameters

The machine learning model processes the following feature vectors:

| Feature Name | Type | Description | Example Values | 
| ----- | ----- | ----- | ----- | 
| `gpu_score` | Numerical | Synthetic GPU Benchmark Score | `2200` (Basic), `5000` (Mid-range), `8500` (High-end) | 
| `cpu_cores` | Numerical | Total Physical CPU Cores | `4`, `6`, `8`, `12` | 
| `ram_gb` | Numerical | System RAM capacity in Gigabytes | `8`, `16`, `32` | 
| `resolution` | Categorical | Target display resolution | `1080p`, `1440p`, `4K` | 
| `game` | Categorical | Selected AAA or Esports game | `GTA 5`, `Cyberpunk 2077`, `Valorant` | 

## 🔮 Future Enhancements

* \[ \] Interactive Chart.js graphs comparing system specs vs target FPS curves.

* \[ \] Automated GPU score lookup dropdown based on model names (e.g., RTX 3060, GTX 1650).

* \[ \] Automated system specs detection via client-side JavaScript / WebGL APIs.

## 🧑‍💻 Author

**Muhammad Ezaan**

*BS AI & Robotics Student*

* **GitHub:** [@Ezaan-Yashkun](https://github.com/Ezaan-Yashkun)