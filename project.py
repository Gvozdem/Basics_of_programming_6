from flask import Flask, render_template, request, make_response

answer = {
    "yes": 0, "no": 0, "notsure": 0
}
answers = {
    "yes": "Вы добряк", "no": "Вы злюка", "notsure": "Вы леприкон"
}
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def show_questions():
    if "voted" in request.cookies and request.cookies["voted"] == "OK":
        return "Вы уже проголосовали"
    else:
        return render_template("questions.html")


@app.route("/results", methods=["GET", "POST"])
def process_results():
    if request.method == "GET":
        return render_template("answers.html", answers=answer)

    if request.method == "POST":
        if "test-1" in request.form:
            if request.form["test-1"] == "yes":
                answer["yes"] += 1
            elif request.form["test-1"] == "no":
                answer["no"] += 1
            elif request.form["test-1"] == "notsure":
                answer["notsure"] += 1

        if "test-2" in request.form:
            if request.form["test-2"] == "yes":
                answer["yes"] += 1
            elif request.form["test-2"] == "no":
                answer["no"] += 1
            elif request.form["test-2"] == "notsure":
                answer["notsure"] += 1

        if "test-3" in request.form:
            if request.form["test-3"] == "yes":
                answer["yes"] += 1
            elif request.form["test-3"] == "no":
                answer["no"] += 1
            elif request.form["test-3"] == "notsure":
                answer["notsure"] += 1

        if "test-4" in request.form:
            if request.form["test-4"] == "yes":
                answer["yes"] += 1
            elif request.form["test-4"] == "no":
                answer["no"] += 1
            elif request.form["test-4"] == "notsure":
                answer["notsure"] += 1

        if answer["yes"] > answer["no"] and answer["yes"] > answer["notsure"]:
            response = make_response(render_template("answers.html", result=answers["yes"]))
            response.set_cookie("voted", "OK")
            return response
        elif answer["no"] > answer["yes"] and answer["no"] > answer["notsure"]:
            response = make_response(render_template("answers.html", result=answers["no"]))
            response.set_cookie("voted", "OK")
            return response
        else:
            response = make_response(render_template("answers.html", result=answers["notsure"]))
            response.set_cookie("voted", "OK")
            return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4321)
