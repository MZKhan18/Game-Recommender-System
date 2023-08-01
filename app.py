import streamlit as st
import pickle
import pandas as pd

def recommend1(app):
    app_index = game_df[game_df['name'] == app].index[0]
    dist = simi[app_index]
    app_list = sorted(list(dist),reverse = True, key = lambda x: x[1])[0:5]
    names = []
    icon = []
    rating =[]
    count = []
    link = []
    for i in app_list:
        names.append(game_df.iloc[i[0]]['name'])
        icon.append(game_df.iloc[i[0]]['icon'])
        rating.append(game_df.iloc[i[0]]['rating'])
        count.append(game_df.iloc[i[0]]['count'])
        link.append(game_df.iloc[i[0]]['URL'])

    return names, icon, rating , count, link

st.title('Game Recommender System')

game = pickle.load(open('game_dict.pkl','rb'))
game_df = pd.DataFrame(game)
simi = pickle.load(open('similarity.pkl','rb'))
game_df.fillna('NA',inplace=True)

game_name = st.selectbox('select game',game_df['name'].values)

if st.button('Recommend Similar Games'):
    names, icon, rating, count, link = recommend1(game_name)
    col0,col1,col2,col3, col4 = st.columns(5)
    with col0:
        st.image(icon[0])
        st.header(names[0])
        st.subheader('Rating : '+str(rating[0]))
        st.subheader('Downloads : '+str(count[0]))
        st.subheader('Game Link:')
        st.write(link[0])

    with col1:
        st.image(icon[1])
        st.header(names[1])
        st.subheader('Rating : '+str(rating[1]))
        st.subheader('Downloads : '+str(count[1]))
        st.subheader('Game Link:')
        st.write(link[1])

    with col2:
        st.image(icon[2])
        st.header(names[2])
        st.subheader('Rating : '+str(rating[2]))
        st.subheader('Downloads : ' + str(count[2]))
        st.subheader('Game Link:')
        st.write(link[2])

    with col3:
        st.image(icon[3])
        st.header(names[3])
        st.subheader('Rating : '+str(rating[3]))
        st.subheader('Downloads : ' + str(count[3]))
        st.subheader('Game Link:')
        st.write(link[3])

    with col4:
        st.image(icon[4])
        st.header(names[4])
        st.subheader('Rating : '+str(rating[4]))
        st.subheader('Downloads : ' + str(count[4]))
        st.subheader('Game Link:')
        st.write(link[4])