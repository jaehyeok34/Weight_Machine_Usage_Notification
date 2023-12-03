from flask import (
    Flask,
    jsonify as fJsonify,
    request as fReq,
    render_template,
)
from repository import Repository as repo
from flask_sqlalchemy import SQLAlchemy
from databaseModel import SensorData
from mainApp import app 

@app.route('/')
def home():
    # 데이터베이스에서 모든 센서 데이터 가져오기
    sensor_data: list[SensorData] = SensorData.query.all()

    print(sensor_data[0].id)

    return "Hello"

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