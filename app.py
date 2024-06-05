import os
from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/groq', methods=['POST'])
def handle_groq_request():
    if request.is_json:
        data = request.get_json()
        print("Received Groq request:", data)

        # Process the Groq request
        try:
            messages = [
                {
                    "role": "user",
                    "content": data.get("requestData", "")
                }
            ]

            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"
            )

            response = {
                "status": "success",
                "message": "Groq request processed successfully",
                "received_data": data,
                "groq_response": chat_completion.choices[0].message.content
            }
            return jsonify(response), 200

        except GroqError as e:
            return jsonify({"error": "An error occurred while processing the Groq request", "details": str(e)}), 500

        except Exception as e:
            return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

    else:
        return jsonify({"error": "Invalid request, JSON expected"}), 400

if __name__ == '__main__':
    app.run(debug=True)
