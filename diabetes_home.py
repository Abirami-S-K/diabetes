import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):
  st.header('Diabetes Prediction App')
  st.markdown('Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.')
    # Set the title to the home page contents.
    
    # Provide a brief description for the web app.


    # Add the 'beta_expander' to view full dataset 
  st.header('View Data')
  with  st.beta_expander('View data set') :
    st.table(diabetes_df)

    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
  st.subheader("Columns Description:")
  beta_col_1,beta_col_2,beta_col_3=st.beta_columns(3)
  with beta_col_1:
    if st.checkbox('Show all column names'):
      st.table(list(diabetes_df.columns))
  with beta_col_2:
    if st.checkbox('View columns data type'):
      st.table(diabetes_df.dtype())
  with beta_col_3:
    if st.checkbox('View column data'):
      col_data=st.selectbox('Select column',(diabetes_df.columns))
      st.write(diabetes_df[col_data])