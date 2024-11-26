from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    try:
         
        
        # Run the Python script
        subprocess.Popen(["python", "AiVirtualMouseProject.py"])
        return "Gesture Control started successfully!", 200
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
