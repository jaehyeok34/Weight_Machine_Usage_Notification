from flask import (
    Flask,
    jsonify as fJsonify,
    request as fReq,
)
from repository import Repository as repo

app = Flask(__name__)

@app.route("/save", methods = ["POST"])
def saveDataToDB():
    try:
        req = repo(**fReq.get_json())

        # TODO: DB에 데이터 저장 구현

    except Exception as e:
        print(e)

def main() -> None:
    port = 3400

    app.run(
        port    =   port,
        debug   =   True,
    )

if __name__ == "__main__":
    main()