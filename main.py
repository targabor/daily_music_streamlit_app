import streamlit as sl
import snowflake_functions
import pandas as pd
import webbrowser

sl.set_page_config(page_title='Schema music', page_icon='🎵')

snowflake_secrets = sl.secrets['snowflake']

# Interactive table based on Snowflake
all_track_data = snowflake_functions.get_all_track_data(snowflake_secrets)
all_track_data.set_index('SONG TITLE', inplace=True)
search_title = sl.text_input('Search by track name')
if search_title:
    all_track_data = all_track_data.loc[all_track_data.index.str.contains(
        search_title, case=False)]

all_artist_names = all_track_data['ARTIST'].unique()
artist_options = [''] + list(all_artist_names)
selected_artist = sl.selectbox('Search by artist name', artist_options)

if selected_artist:
    all_track_data = all_track_data.loc[all_track_data['ARTIST']
                                        == selected_artist]

# Change this list to adjust the options
# Change this list to adjust the options
rows_per_page_options = [5, 10, 20, 50, 100]
rows_per_page = sl.selectbox("Rows per page:", options=rows_per_page_options)

num_rows = all_track_data.shape[0]
num_pages = num_rows // rows_per_page + (num_rows % rows_per_page > 0)

page = sl.slider("Page", min_value=1, max_value=num_pages, value=1)

start_index = (page - 1) * rows_per_page
end_index = min(page * rows_per_page, num_rows)

sl.write(f"Displaying rows {start_index+1} to {end_index} of {num_rows}")
df = all_track_data.iloc[start_index:end_index]
for index, row in df.iterrows():
    sl.write(row['SONG TITLE'], row['ARTIST'], row['POPULARITY'])
    if sl.button("Open URL", key=index):
        webbrowser.open_new_tab(row['SONG URL'])


# Email Subscription part
sl.write('If you want to get weekly updates of #daily-music and get to know a bunch of fun stats, subscribe to the mailing list!')
email = sl.text_input('', value='example@example.com')
if sl.button('Subscribe'):
    sl.write(snowflake_functions.add_email_to_mailing_list(
        email, **sl.secrets["snowflake"]))
