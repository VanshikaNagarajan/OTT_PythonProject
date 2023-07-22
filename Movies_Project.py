# importing libraries
import pandas as pd

#retrieving data from csv file
df_amazon_prime = pd.read_csv('amazon_prime.csv')
print("df_amazon_prime is my amazon prime data", df_amazon_prime)

df_netflix = pd.read_csv('netflix.csv')
print("df_netflix is netflix data", df_netflix)

df_disney_plus = pd.read_csv('disney_plus.csv')
print("df_disney_plus is disney plus data", df_disney_plus)

#to showcase the data (head() shows the
df_amazon_prime.head()
df_netflix.head()
df_disney_plus.head()

specific_coloumn = df_amazon_prime[['show_id', 'type', 'title', ]]
print(specific_coloumn)

specific_coloumn1 = df_netflix[['show_id', 'type', 'title', ]]
print(specific_coloumn1)

specific_coloumn2 = df_disney_plus[['show_id', 'type', 'title', ]]
print(specific_coloumn2)

# to check if the show is present in any of the 3 OTT Platforms
def find_show_details(show_title):
    show_title = show_title.lower().strip()
    if show_title in df_netflix['title'].str.lower().values:
        streaming_service = "Netflix"
        show_df = df_netflix

    elif show_title in df_amazon_prime['title'].str.lower().values:
        streaming_service = "Amazon Prime"
        show_df = df_amazon_prime

    elif show_title in df_disney_plus['title'].str.lower().values:
        streaming_service = "Disney Plus"
        show_df = df_disney_plus

    else:
        print(f"Show '{show_title}' not found in any service")
        return

# To show the details of the specified show/movie
    details_show = show_df[show_df['title'].str.lower() == show_title]
    if not details_show.empty:
        details = details_show.iloc[0]
        print("Streaming_service: ", streaming_service)
        print("Title: ", details['title'])
        print("Director: ", details['director'])
        print("Cast: ", details['cast'])
        print("Date Added:", details['date_added'])
        print("Release Year:", details['release_year'])
        print("Rating:", details['rating'])
        print("Duration:", details['duration'])
        print("Listed In:", details['listed_in'])
        print("Description:", details['description'])
    else:
        print(f"Details for the show '{show_title}' not found.")


# to ask the user to specify the show or movie title
user_input = input("Enter the Show Title").lower().strip()
find_show_details(user_input)
