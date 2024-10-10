from flask import Flask
from data.data_loader import load_from_csv_to_db
from data.data_getter import get_accidents_by_zone
from routes.accident_bp import accident_bp
app = Flask(__name__)
app.register_blueprint(accident_bp, url_prefix='/accidents')
# print(get_accidents_by_zone("225"))
# load_from_csv_to_db(r"C:\Users\yechezkel\PycharmProjects\chicagoCarAccidents\csv_files\Traffic_Crashes_20k_rows.csv")

@app.route('/')
def home_page():
    return 'Wellcome to the home page!'


if __name__ == '__main__':
    app.run()
