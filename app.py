from flask import Flask, request, jsonify
from parser import parse_log
from rules import detect_issue

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    log = parse_log(data.get("log", ""))

    result = detect_issue(log)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
