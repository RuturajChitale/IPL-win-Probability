import streamlit as st
import pickle
import pandas as pd



st.title('IPL win Probability')
teams = ['Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
       'Royal Challengers Bengaluru', 'Sunrisers Hyderabad',
       'Rajasthan Royals', 'Delhi Capitals', 'Punjab Kings',
       'Lucknow Super Giants', 'Gujarat Titans']
city = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Jaipur', 'Chennai',
       'Kolkata', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Dharamsala', 'Pune', 'Hyderabad', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Unknown', 'Cuttack', 'Visakhapatnam', 'Bengaluru',
       'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati',
       'Mohali', 'New Chandigarh']

pipe = pickle.load(open('pipe.pkl', 'rb'))

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting Team', teams)
with col2:
    bowling_team = st.selectbox('Select Bowling Team', teams)

selected_city = st.selectbox('Selected city is ', sorted(city))

target = st.number_input( 'Target ')
col3, col4 ,col5= st.columns(3)
with col3:
       score = st.number_input('Score')
with col4:
       overs = st.number_input('Overs Completed')
with col5:
       Wickets = st.number_input('Wickets_out')
if st.button('Predict probability'):
       runs_left = target -score
       balls_left = 120 - overs*6
       wickets_left = 10 - Wickets
       crr = score / overs if overs > 0 else 0
       rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0
       input_df = pd.DataFrame({
              'batting_team': [batting_team],
              'bowling_team': [bowling_team],
              'city': [selected_city],
              'runs_left': [runs_left],
              'balls_left': [balls_left],
              'wickets_left': [wickets_left],
              'total_runs_x': [target],
              'crr': [crr],
              'rrr': [rrr]
       })
       result = pipe.predict_proba(input_df)
       loss = round(result[0][0] * 100, 2)
       win = round(result[0][1] * 100, 2)

       st.header(f"{batting_team} Win Probability: {win}%")
       st.header(f"{bowling_team} Win Probability: {loss}%")


