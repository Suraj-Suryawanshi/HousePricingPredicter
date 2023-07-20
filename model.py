# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder, LabelEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.tree import DecisionTreeRegressor
# import pickle

# # Load the dataset
# data = pd.read_csv('MagicBricks.csv')  # Replace 'MagicBricks.csv' with your actual dataset file
# data = data.dropna()

# # Select relevant features and target variable
# numeric_features = ['Area', 'BHK', 'Bathroom', 'Parking', 'Per_Sqft']
# categorical_features = ['Furnishing', 'Status', 'Transaction', 'Type']
# label_encoded_features = ['Locality']

# # Data preprocessing
# # Perform any necessary data cleaning and scaling here

# # Merge unseen labels into a single category 'Unknown' for 'Locality'
# min_frequency = 10  # Define a threshold frequency for considering labels as 'unseen'
# loc_freq = data['Locality'].value_counts()
# unseen_labels = loc_freq[loc_freq < min_frequency].index
# data['Locality'] = data['Locality'].apply(lambda x: 'Unknown' if x in unseen_labels else x)

# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(data[numeric_features + categorical_features + label_encoded_features], data['Price'], test_size=0.2, random_state=42)

# # One-hot encoding for categorical variables
# preprocessor = ColumnTransformer(
#     transformers=[('cat', OneHotEncoder(), categorical_features)],
#     remainder='passthrough'
# )
# X_train_encoded = preprocessor.fit_transform(X_train)
# X_test_encoded = preprocessor.transform(X_test)

# # Label encoding for 'Locality' column
# label_encoder = LabelEncoder()
# X_train_encoded[:, -1] = label_encoder.fit_transform(X_train_encoded[:, -1])
# X_test_encoded[:, -1] = label_encoder.transform(X_test_encoded[:, -1])

# # Decision tree model training
# model = DecisionTreeRegressor(random_state=42)
# model.fit(X_train_encoded, y_train)

# # Pickle the model
# with open('model.pkl', 'wb') as file:
#     pickle.dump(model, file)


import pickle
import pandas as pd

def encode_house_features(house_features):
    with open('./model/pre.pkl', 'rb') as file:
        preprocessor = pickle.load(file)

    with open('./model/label.pkl', 'rb') as file:
        label_encoder = pickle.load(file)

    # Define the numeric and categorical feature names
    numeric_features = ['Area', 'BHK', 'Bathroom', 'Parking', 'Per_Sqft']
    categorical_features = ['Furnishing', 'Status', 'Transaction', 'Type']
    label_encoded_features = ['Locality']

    # Convert house_features into a DataFrame
    house_features_df = pd.DataFrame([house_features], columns=numeric_features + categorical_features + label_encoded_features)

    # One-hot encoding for categorical variables
    house_features_encoded = preprocessor.transform(house_features_df)

    # Label encoding for 'Locality' column
    try:
        house_features_encoded[:, -1] = label_encoder.transform(house_features_encoded[:, -1])
    except ValueError as e:
        # Handle unseen labels by merging them into a single category 'Unknown'
        loc_label = house_features_encoded[0, -1]
        loc_label = 'Unknown' if loc_label not in label_encoder.classes_ else loc_label
        house_features_encoded[0, -1] = label_encoder.transform([loc_label])[0]
    
    return house_features_encoded

def predict_output(house_features):
    with open('./model/model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Use the preprocessor and label_encoder to encode the house_features
    encoded_house_features = encode_house_features(house_features)

    # Make predictions using the loaded model
    predicted_price = model.predict(encoded_house_features)

    return predicted_price[0]
