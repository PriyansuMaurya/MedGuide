from flask import Blueprint,render_template, request
import dill
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


views = Blueprint('views',__name__)


@views.route('/', methods=['GET','POST'])
def index():
        symptoms = get_symptoms()

        if request.method == 'POST':
                age = request.form.get('age')
                sex = request.form.get('sex')
                symptom = request.form.get('symptom')
                 

                df = pd.read_csv('notebook/data/disease_with_132_features.csv')
                df_drop_target = df.drop(['prognosis'],axis =1)
                numerical_columns = np.array(df_drop_target.columns)
                            
                input_values = {
                        "itching" : [1],
                        "skin_rash" : [1],
                        "nodal_skin_eruptions" : [0],
                        "inflammatory_nails" : [1],
                        "chills" : [0],
                        "yellow_crust_ooze": [0],
                        "blister": [1]
                }

                default_input_values = {feature :[0] for feature in numerical_columns}

                # Updating the default input values with the symptoms that are given by the patients.
                default_input_values.update(input_values)
                
                # converting from 2d to 1d
                all_values = [value[0] for value in default_input_values.values()]

                if 1 not in all_values:
                        print("Enter atleast one symptom:")
                # else:
                input_df = pd.DataFrame(default_input_values)

                model = dill.load(open('artifacts/preprocessor_v1.pkl', 'rb'))
                final_model = dill.load(open('artifacts/best_model_v1.pkl', 'rb'))
                
                # Transform the input data
                data_scaled = model.transform(input_df)

                # Evaluate the performance of the model
                # print(data_scaled)

                # Make predictions
                pred = final_model.predict(data_scaled)
                diseases = get_diseases()

                index = np.where(pred[0] > 0.5)[0][0]

                # return f"{diseases[index][10:]}"
                return f"{symptom}"
                # return render_template(
                #         'possible_disease.html', 
                #         title="Possible disease",
                #         possible_disease = diseases[index]
                #         )
                

        return render_template('tell_symptoms.html', title="Possible disease", symptoms_list = symptoms)


def get_diseases():

        train_df = pd.read_csv('artifacts/train.csv')

        target_column_name = "prognosis"
        
        target_feature_train_df = train_df[[target_column_name]]

        # Apply one-hot encoding to the target feature
        one = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform='pandas')

        output_feature_train_df = one.fit_transform(target_feature_train_df)

        # Decoding the disease column
        diseases = np.array([column for column in  output_feature_train_df.columns])

        return diseases
    
def get_symptoms():

        train_df = pd.read_csv('artifacts/train.csv')

        # target_column_name = "prognosis"
        
        # train_feature_df = train_df.drop(target_column_name)

        symptoms = np.array([column for column in  train_df.columns])

        return symptoms


