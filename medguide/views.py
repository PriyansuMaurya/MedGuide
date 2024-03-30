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
                symptom = request.form.getlist('symptom')

                
                # print(f'Selected Symptom: {symptom}')
                df = pd.read_csv('notebook/data/disease_with_132_features.csv')
                df_drop_target = df.drop(['prognosis'],axis =1)
                numerical_columns = np.array(df_drop_target.columns)
                            
                if symptom is not None and isinstance(symptom, (list, tuple)):
                        input_values = {
                                value : [2] for value in symptom
                        }
                else:
                        input_values = {}

                
                default_input_values_list = {}

                default_input_values = {feature :[0] for feature in numerical_columns}
                # print(symptom)

                # Updating the default input values with the symptoms that are given by the patients.
                default_input_values.update(input_values)
                
                # converting from 2d to 1d
                all_values = [value[0] for value in default_input_values.values()]

                if 1 not in all_values:
                        print("Enter atleast one symptom:")
                # else:
                input_df = pd.DataFrame(default_input_values)

                # model = dill.load(open('artifacts/preprocessor_v1.pkl', 'rb'))
                random_forest = dill.load(open('artifacts/best_model_v2.pkl', 'rb'))
                k_neighbour = dill.load(open('artifacts/K-Neighbors_v2.pkl', 'rb'))
                svm = dill.load(open('artifacts/svm_v2.pkl', 'rb'))

                # Make predictions
                pred_1 = random_forest.predict(input_df)
                pred_2 = k_neighbour.predict(input_df)
                pred_3 = svm.predict(input_df)

                possible_disease = [pred_1, pred_2, pred_3]
                # unique_words = list(dict.fromkeys(possible_disease))

                unique_list = []
                [unique_list.append(x) for x in possible_disease if x not in unique_list]
                
                return render_template(
                        'possible_disease.html', 
                        title="Possible disease",
                        possible_disease = unique_list
                        )
                

        return render_template('tell_symptoms.html', title="tell symptoms", symptoms_list = symptoms)


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

        return np.sort(symptoms)


