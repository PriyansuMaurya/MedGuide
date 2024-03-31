from flask import Blueprint,render_template, request

extents = Blueprint('extents',__name__)



@extents.route("/suggestions", methods=['GET', 'POST'])
def suggestions():
        # clicked_button_name
        if request.method == 'POST':
                disease = request.form.get('clicked_button_name')
                
                return render_template('suggestions.html', title="Suggestions", prescription = disease)
                
        # return f"{'shivam'}"

@extents.route("/faqs", methods=['GET', 'POST'])
def faqs(): 
       
        return render_template('faqs.html', title="Faqs")



