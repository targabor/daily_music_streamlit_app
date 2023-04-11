import snowflake.connector
import helper
import pandas as pd


def add_email_to_mailing_list(email: str, secrets):
    if helper.email_is_valid(email) and email != 'example@example.com':
        with snowflake.connector.connect(secrets) as con:
            hashed_email = helper.hash_email(email)
            with con.cursor() as cur:
                cur.execute(
                    "INSERT INTO CONSOLIDATED.subscribers (ID, EMAIL) VALUES (%s,%s);", (hashed_email, email))
                return f'subscribed with {email}'
    else:
        return 'please add a valid email address'


def get_all_track_data(secrets) -> pd.DataFrame:
    """It returns all stored track in a DataFrame object

    Returns:
        pd.DataFrame: It contains all the track data
    """
    select_query = '''  SELECT distinct ST.TITLE as "Song Title", 
                                        IFNULL(A.NAME, 'unknown') as Artist, 
                                        ST.POPULARITY as Popularity FROM SPOTIFY_TRACK ST
                        LEFT JOIN ARTIST A ON A.ID = ST.ARTIST_ID;'''
    query_result = None
    with snowflake.connector.connect(secrets) as con:
        query_result = pd.read_sql(select_query, con)

    return query_result if query_result is not None else pd.DataFrame()
