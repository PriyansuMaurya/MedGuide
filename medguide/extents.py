from flask import Blueprint,render_template, request
import json
import os
extents = Blueprint('extents',__name__)

# Get the current directory of the Python file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to suggestion.json
JSON_FILE_PATH = os.path.join(current_directory, "templates", "suggestion.json")


@extents.route("/suggestions", methods=['GET', 'POST'])
def suggestions():
        # Open the JSON file
        # with open('/workspaces/MedGuide/medguide/templates/suggestion.json', 'r') as file:
        with open(JSON_FILE_PATH, 'r') as file:   
        # Load JSON data into a Python dictionary
                disease_data = json.load(file)         
        # clicked_button_name                      
        if request.method == 'POST':
                disease = request.form.get('clicked_button_name')[2:-2]
                def get_recommendations(my_disease):
        # Dummy function to get recommendations based on disease
                        recommendations = {}
                
                        # Get recommendations based on the provided disease
                        if my_disease in disease_data:
                                recommendations["prevention"] = disease_data[my_disease]["prevention"]
                                recommendations["medication"] = disease_data[my_disease]["medication"]
                                recommendations["overview"] = disease_data[my_disease]["overview"]

                        else:
                                recommendations["prevention"] = ["No specific prevention measures found."]
                                recommendations["medication"] = ["No specific medications found."]
                                recommendations["overview"] = ["No overview found."]

                        return recommendations
                                
                return render_template('suggestions.html', title="Suggestions", prescription = get_recommendations(disease), disease_name=disease)
                
@extents.route("/faqs", methods=['GET', 'POST'])
def faqs(): 
       
        return render_template('faqs.html', title="Faqs")



