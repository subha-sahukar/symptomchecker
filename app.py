from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    symptoms = request.form['symptoms'].lower()
    possible_diseases = {
        'fever': ['Flu', 'COVID-19', 'Common Cold'],
        'cough': ['Flu', 'COVID-19', 'Common Cold'],
        'headache': ['Migraine', 'Tension Headache', 'Flu'],
        'fatigue': ['Anemia', 'Chronic Fatigue Syndrome', 'Hypothyroidism']
    }
    matched_diseases = set()
    for symptom in possible_diseases:
        if symptom in symptoms:
            matched_diseases.update(possible_diseases[symptom])
    return render_template('results.html', diseases=matched_diseases)

if __name__ == '__main__':
    app.run(debug=True)
