from flask import Flask, render_template, request
import os  

app = Flask(__name__, static_folder="static")


def load_codes():
    codes = {}
    with open("codes.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                codes[parts[0]] = {"riddle": parts[1], "next_code": parts[2]}
    return codes

codes = load_codes()

@app.route("/", methods=["GET", "POST"])
def index():
    riddle = None
    next_code_partial = None
    error = None

    if request.method == "POST":
        entered_code = request.form.get("code")
        if entered_code in codes:
            riddle = codes[entered_code]["riddle"]
            full_next_code = codes[entered_code]["next_code"]

            # Show only first 50% of the next code
            half_length = len(full_next_code) // 2
            next_code_partial = full_next_code[:half_length] + "****"  
        else:
            error = "Guys You Are PUCSDIan Think Again & Try Again!!!"

    return render_template("index.html", riddle=riddle, next_code=next_code_partial, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
	
