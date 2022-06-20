#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries and set client_id
import requests
import json
import urllib
import MAL_Cookbook
import time

client_id = "0bd76a18d2f4d2bb27ca27105be29188"

base_url = "https://api.myanimelist.net/v2/"
auth_header = {"X-MAL-CLIENT-ID" : client_id}


# In[2]:


#Function where you give a MAL username and it returns the users top 5 most watched genres

def topGenres(username):
    genres = MAL_Cookbook.get_genre_preferences(client_id, username)
    
#add each genre to the genreList as a tuple (genre, numer of shows in that genre)
    genreList = []
    for index in genres:
       # print(genres[index]['genre']['name'], genres[index]['count'])
        genreList.append(tuple([genres[index]['genre']['name'], genres[index]['count']]))

    gl = genreList.sort(key = lambda x: -x[1]) 

    #sort the genre and return the top 5
    
    TopG = []
    for gen in genreList:
        TopG.append(gen[0])                  
    return(TopG[:5])

#Function that you input a MAL username and it will return the median year of the shows they watched

def medianYear(username):
    yl = MAL_Cookbook.get_vintage_preferences(client_id, username)

    yearList = []
    medianlist = []
    for index in yl:
      #  print(yl[index]['count'])
       # print(yl[index]['season']['year'])
        times = yl[index]['count']
        #Add each show year to a list
        while times > 0:
            medianlist.append(yl[index]['season']['year'])
            times = times - 1
       # print(genres[index]['genre']['name'], genres[index]['count'])
       
    #sort the list 
    medianlist.sort()
   # return the median
    return(medianlist[int(len(medianlist)/2)])

#function that you input a MAL username and a desired score
#The function will return all show id's on a MAL user list above the entered score  

def topShowsOnList(username, rat):
    rating = []
    animelist = MAL_Cookbook.get_user_list_ids(client_id, username)
    for a in animelist:
        for al in animelist[a]:
            score = al['list_status']['score']
            sid = al['node']['id']
            if score >= rat:
                rating.append(sid)
    return(rating)

def medianNumEpisodes(username):
    #listOfShows = topShowsOnList(username, 0)
    listOfNums = []
    num = MAL_Cookbook.get_user_list_ids(client_id, username, fields='num_episodes')['data']
    for node in num:
        el = int(node['node']['num_episodes'])
        if el != 0:
            listOfNums.append(el)
    listOfNums.sort()
    return(listOfNums[int(len(listOfNums)/2)])


# In[3]:


#This block of code will get information on a user that you select
def getUserInformation(username):

    my = medianYear(username)
    print("Median Year:", my)
    tg = topGenres(username)
    print("Top genres:", tg)
    userratedshows = topShowsOnList(username, 8)
    #print(len(userratedshows))
    userIdList = topShowsOnList(username, 0)
   # print(len(userIdList))
    userMedian = medianNumEpisodes(username)
    print("Median Episodes:", userMedian)

    return my, tg, userratedshows, userIdList, userMedian


# In[4]:

def getRecommendationsNewUser(tg, yearw, genrew, userRecSW, lengthw):
    my = 2015
    userMedian = 25
    storedTopShows = []
    topshows = MAL_Cookbook.get_top_shows_stat(client_id, 10000, stat="start_season,num_episodes,genres")
    for tsn in topshows:
        try:
            storedTopShows.append(tuple([tsn['id'],tsn['start_season'],tsn['genres'],tsn['num_episodes']]))
        except:
            blank = 1
    #print(storedTopShows)
    
  #This section of code will create the recommendations
    cc = 0
    rScores = []
#go through ever show in the top
    for showId in storedTopShows:
        currentid = showId[0]
        showyear = showId[1]
        genress = showId[2]
        numberEpisodes = showId[3]
   # print(showId)
    #showyear = get_show_stats(client_id, show_id=showId, content_type='anime', stat='start_season')
    #genres = get_genre(client_id, show_ids=showId, content_type='anime')

    #create a year score by taking away 10% for each year away from median
        yearScore = 10 - abs(my - showyear['year'])
        if yearScore < 0:
            yearScore = 0
   # print("Year Score", yearScore)

#create genrescore by adding points for each genre a show has in a users top genres
        genreScore = 0
        y = 0
        for i in genress:
        #while y < len(genress[i]):
            g =i['name']
            if g in tg:
                ind = tg.index(g)
                genreScore = genreScore + 5 - ind
                #print(5-ind)
                y = y + 1
    #print("OGgenreScore", genreScore)

        genreScore = genreScore / 15
        genreScore = genreScore * 10

    #print("genreScore", genreScore)
    
    #gives a point if a topshow is a user recommended show on mal
        userRecScore = 0
        #print(userRecScore)
    #print(currentid)
    
    
        olengthScore =  abs(userMedian - numberEpisodes)
        if olengthScore > 20:
            olengthScore = 20
        lengthScore = (olengthScore / 20)
        lengthScore = lengthScore * 10
        lengthScore = 10 - lengthScore
    
    #print(olengthScore,lengthScore)
    
    #Calculates the shows rating with different weights
        rPoint = (yearScore * yearw) + (genreScore * genrew) + (userRecScore *  userRecSW) + (lengthScore * lengthw)
    
   # print(showId, rPoint)
        rScores.append(tuple([showId[0], rPoint]))
        cc = cc + 1
   # print(cc)
#Removes shows you have watched
    sanScores = []
    f = 0

#print(f)
    rwww = sanScores.sort(key = lambda x: -x[1]) 

#Prints your top 10 shows
    c = 0
    while c < 10:
        show = MAL_Cookbook.get_show_stats(client_id, show_ids=rScores[c][0], content_type='anime')
        for k in show:
            print(c + 1, k['title'], rScores[c][1])
        c = c + 1

    return rScores



def getRecommendations(username, yearw = .20, genrew = .60, userRecSW = .20, lengthw = 0):
    my, tg, userratedshows, userIdList, userMedian = getUserInformation(username)
    storedTopShows = []
    topshows = MAL_Cookbook.get_top_shows_stat(client_id, 10000, stat="start_season,num_episodes,genres")
    for tsn in topshows:
        try:
            storedTopShows.append(tuple([tsn['id'],tsn['start_season'],tsn['genres'],tsn['num_episodes']]))
        except:
            blank = 1
    #print(storedTopShows)
    
  #This section of code will create the recommendations
    cc = 0
    rScores = []
#go through ever show in the top
    for showId in storedTopShows:
        currentid = showId[0]
        showyear = showId[1]
        genress = showId[2]
        numberEpisodes = showId[3]
   # print(showId)
    #showyear = get_show_stats(client_id, show_id=showId, content_type='anime', stat='start_season')
    #genres = get_genre(client_id, show_ids=showId, content_type='anime')

    #create a year score by taking away 10% for each year away from median
        yearScore = 10 - abs(my - showyear['year'])
        if yearScore < 0:
            yearScore = 0
   # print("Year Score", yearScore)

#create genrescore by adding points for each genre a show has in a users top genres
        genreScore = 0
        y = 0
        for i in genress:
        #while y < len(genress[i]):
            g =i['name']
            if g in tg:
                ind = tg.index(g)
                genreScore = genreScore + 5 - ind
                #print(5-ind)
                y = y + 1
    #print("OGgenreScore", genreScore)

        genreScore = genreScore / 15
        genreScore = genreScore * 10

    #print("genreScore", genreScore)
    
    #gives a point if a topshow is a user recommended show on mal
        userRecScore = 0
        if currentid in userratedshows:
            userRecScore = 10
        #print(userRecScore)
    #print(currentid)
    
    
        olengthScore =  abs(userMedian - numberEpisodes)
        if olengthScore > 20:
            olengthScore = 20
        lengthScore = (olengthScore / 20)
        lengthScore = lengthScore * 10
        lengthScore = 10 - lengthScore
    
    #print(olengthScore,lengthScore)
    
    #Calculates the shows rating with different weights
        rPoint = (yearScore * yearw) + (genreScore * genrew) + (userRecScore *  userRecSW) + (lengthScore * lengthw)
    
   # print(showId, rPoint)
        rScores.append(tuple([showId[0], rPoint]))
        cc = cc + 1
   # print(cc)

#Removes shows you have watched
    sanScores = []
    f = 0
    for s in rScores:
        if s[0] in userIdList:
            f = f + 1
        else:
            sanScores.append(s)
#print(f)
    rwww = sanScores.sort(key = lambda x: -x[1]) 

#Prints your top 10 shows
    c = 0
    while c < 10:
        show = MAL_Cookbook.get_show_stats(client_id, show_ids=sanScores[c][0], content_type='anime')
        for k in show:
            print(c + 1, k['title'], sanScores[c][1])
        c = c + 1

    return sanScores


# In[9]:


#s = getRecommendations("happydr", .20, .60, .10, .10)
#username, year, genre, year, userRecScore, length
#getRecommendations("spicece")


# print(len(storedTopShows))

# In[ ]:




