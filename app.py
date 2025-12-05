from flask import Flask, request, render_template
from game_engine import process_step

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    state = request.form.get("state", "{}")
    user_input = request.form.get("user_input", "")

    new_state, output_text = process_step(state, user_input)

    return render_template(
        "game.html",
        state=new_state,
        output_text=output_text
    )

if __name__ == "__main__":
    app.run()
