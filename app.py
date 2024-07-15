import streamlit as st
import pickle
import seaborn as sns

# Load the pickled model
model = pickle.load(open('model.pkl', 'rb'))

# Define the main function
def main():
    # Create a sidebar with two options: Prediction and EDA
    option = st.sidebar.selectbox('Select Option', ['Prediction', 'EDA'])

    # Prediction
    if option == 'Prediction':
        st.subheader('Honey Price Prediction')

        # Get user input for features
        CS = st.number_input('Color Score (CS)', min_value=1.0, max_value=10.0)
        Density = st.number_input('Density (g/cm^3)', min_value=1.21, max_value=1.86)
        WC = st.number_input('Water Content (%)', min_value=12.0, max_value=25.0)
        pH = st.number_input('pH', min_value=2.50, max_value=7.50)
        EC = st.number_input('Electrical Conductivity (mS/cm)', min_value=0.08, max_value=1.99)
        F = st.number_input('Fructose Level (g)', min_value=20, max_value=50)
        G = st.number_input('Glucose Level (g)', min_value=20, max_value=45)
        Pollen_analysis = st.selectbox('Pollen Analysis', options=df['Pollen_analysis'].unique())
        Viscosity = st.number_input('Viscosity (cP)', min_value=1500, max_value=10000)

        # Convert categorical feature to numerical
        le = LabelEncoder()
        Pollen_analysis_encoded = le.fit_transform([Pollen_analysis])[0]

        # Create a feature vector
        features = [CS, Density, WC, pH, EC, F, G, Pollen_analysis_encoded, Viscosity]

        # Make a prediction
        predicted_price = model.predict([features])

        # Display the predicted price
        st.write('Predicted Price:', predicted_price[0])

    # EDA
    elif option == 'EDA':
        st.subheader('Honey Price Exploratory Data Analysis')

        # Display descriptive statistics of the dataset
        st.write(df.describe())

        # Display a correlation matrix of the dataset
        st.write(df.corr())

        # Display a scatter plot of Price vs. Color Score
        st.write(sns.scatterplot(x='CS', y='Price', data=df))

        # Display a bar plot of average Price by Pollen Analysis
        st.write(sns.barplot(x='Pollen_analysis', y='Price', data=df))

# Run the main function
if __name__ == '__main__':
    main()