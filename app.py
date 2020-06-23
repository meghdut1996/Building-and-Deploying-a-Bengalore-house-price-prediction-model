import flask
from flask import request, render_template
from babel.numbers import format_currency
from flask_babel import Babel
app=flask.Flask(__name__,template_folder='templates')

app.config["DEBUG"]=True

from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    from sklearn.externals import joblib
    model=joblib.load('house_price.ml')
    house_price=model.predict([[int(request.args['place']),
                                int(request.args['sqft']),
                                int(request.args['yearsOld']),
                                int(request.args['floor']),
                                int(request.args['totalFloor']),
                                int(request.args['bhk']),
                                int(request.args['built'])]])
    
    result=str(round(house_price[0],0))
    return format_currency(result,'INR', locale='en_IN').replace(u'\xa0',u' ')

if __name__ == "__main__":
    app.run(debug=True)
    


#render_template('index.html'),,methods=['GET','POST']
