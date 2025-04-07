from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace with your Gemini API key
genai.configure(api_key="Use_API_Key_Here")

# Use a working model from your list
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    prompt = f"""
You're a friendly AI language tutor.
Correct the sentence below, provide a translation, and explain grammar/vocabulary concepts.
Format your reply in clean HTML with sections and bullet points for readability.

Sentence: "{user_input}"
"""


    try:
        response = model.generate_content([prompt])
        reply = response.text.strip()
    except Exception as e:
        reply = f"Sorry, something went wrong: {str(e)}"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
