from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API Running"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        petal_length = float(request.args.get("petal_length"))

        result = "setosa" if petal_length < 2 else "versicolor"
        return jsonify({"prediction": result})
    except:
        return jsonify({"error": "Invalid input"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)