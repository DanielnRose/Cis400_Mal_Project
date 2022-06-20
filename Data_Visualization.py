import Recommendations
import MAL_Cookbook
client_id = "d1ba6c8f42d9abdc2aa2d84fb61702e5"

import requests
import urllib.request
#import matplotlib.pyplot as plt
#from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
from IPython.display import display, HTML

user = 'ohio64'
#recommendations = Recommendations.getRecommendations(user, .20, .60, .10, .10)
    
def visualizeTop5Shows(client_id, recommendations):
    recommendations = recommendations[:5]
    i = 1
    old_top5 = recommendations
    top5_recs = []

    show_pictures = MAL_Cookbook.get_show_pictures(client_id, [tuple[0] for tuple in recommendations])
    for id in show_pictures:
        poster_path = show_pictures[id]['medium']
    poster_urls = [show_pictures[id]['medium'] for id in show_pictures]

    while i <= 5:

        show_id = old_top5[i - 1][0]
        stats = MAL_Cookbook.get_show_stats(client_id, show_id)
        title = stats[0]['title']
        rating = old_top5[i - 1][1]
        #poster_path = 'http://localhost:8888/view/data/rec' +  str(i) + '.jpg'
        poster_path = poster_urls[i - 1]
        top5_recs.append((title, rating, poster_path))
        i += 1

    #print(top5_recs)
    df = pd.DataFrame(top5_recs, columns = ['Title', 'Recommendation Score', 'Poster'])

    df['Poster'] = poster_urls
    # Rendering the dataframe as HTML table
    show(recommendations, df)
    return df #.to_html(escape=False, formatters=dict(Poster=path_to_image_html))

    # Rendering the images in the dataframe using the HTML method.
    HTML(df.to_html(escape=False,formatters=dict(Poster=path_to_image_html)))

    
# Converting links to html tags
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

def show(recommendations, df):
    df = visualizeTop5Shows(client_id, recommendations)
    df.to_html(escape=False, formatters=dict(Poster=path_to_image_html))

    # Rendering posters in dataframe using the HTML
    HTML(df.to_html(escape=False,formatters=dict(Poster=path_to_image_html)))