from flask import Flask,request,render_template


app=Flask(__name__)

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():

        return render_template('predict.html',results="Good")
    

if __name__=="__main__":
    app.run(debug=True)       

