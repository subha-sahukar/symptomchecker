from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

symptoms_data = {
    'head': ['Headache', 'Dizziness', 'Vision problems', 'Nausea', 'Ear pain', 'Sore throat', 'Fever', 'Sinus pressure', 'Facial pain', 'Neck stiffness', 'Scalp tenderness', 'Hair loss', 'Jaw pain', 'Toothache', 'Bleeding gums'],
    'chest': ['Chest pain', 'Shortness of breath', 'Cough', 'Heart palpitations', 'Wheezing', 'Chest tightness', 'Fatigue', 'Dizziness', 'Swollen legs', 'Rapid heartbeat', 'High blood pressure', 'Low blood pressure', 'Fever', 'Chills', 'Night sweats'],
    'abdomen': ['Stomach pain', 'Nausea', 'Vomiting', 'Diarrhea', 'Constipation', 'Bloating', 'Heartburn', 'Indigestion', 'Loss of appetite', 'Jaundice', 'Abdominal swelling', 'Blood in stool', 'Weight loss', 'Fatigue', 'Fever'],
    'leg': ['Leg pain', 'Swelling', 'Cramps', 'Numbness', 'Tingling', 'Weakness', 'Varicose veins', 'Cold feet', 'Discoloration', 'Ulcers', 'Muscle spasms', 'Joint pain', 'Stiffness', 'Bruising', 'Redness']
}

disease_data = {
    frozenset(['Headache', 'Dizziness', 'Vision problems']): 'Migraine',
    frozenset(['Chest pain', 'Shortness of breath', 'Cough']): 'Flu',
    frozenset(['Stomach pain', 'Nausea', 'Vomiting']): 'Food Poisoning',
    frozenset(['Leg pain', 'Swelling', 'Cramps']): 'Deep Vein Thrombosis'
}

@app.route('/')
def home():
    return render_template('index.html', body_parts=symptoms_data.keys())

@app.route('/get_symptoms', methods=['POST'])
def get_symptoms():
    body_part = request.form['body_part']
    symptoms = symptoms_data.get(body_part, [])
    return jsonify(symptoms)

@app.route('/results', methods=['POST'])
def results():
    selected_symptoms = request.form.getlist('symptoms')
    selected_symptoms_set = frozenset(selected_symptoms)
    possible_diseases = [disease for symptoms, disease in disease_data.items() if selected_symptoms_set.issubset(symptoms)]
    return render_template('results.html', diseases=possible_diseases)

if __name__ == '__main__':
    app.run(debug=True)
