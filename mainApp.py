from flask import (
    Flask,
    jsonify as fJsonify,
    request as fReq,
    render_template,
)
from repository import Repository as repo
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus

app = Flask(__name__)

password = "1qaz!@#$%"
encoded_password = quote_plus(password)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{encoded_password}@localhost:3401/weight_machine_log"
db = SQLAlchemy(app)

# @app.route('/')
# def home():
#     # 데이터베이스에서 모든 센서 데이터 가져오기
#     sensor_data = SensorData.query.all()

#     return render_template('home.html', sensor_data=sensor_data)

# @app.route("/save", methods = ["POST"])
# def saveDataToDB():
#     try:
#         req = repo(**fReq.get_json())

#         # TODO: DB에 데이터 저장 구현

#     except Exception as e:
#         print(e)

# def main() -> None:
#     port = 3400

#     app.run(
#         port    =   port,
#         debug   =   True,
#     )

# if __name__ == "__main__":
#     main()