# CIS400Project_MAL
 CIS 400 Project (Spring 2022) - Using the MyAnimeList API to data mine and create usable results.

pip install required extensions 
Start code by running python -i gui.py

Setup
This project requires the following libraries:
- selenium
- pandas
- tkinter
- urllib2
- requests

How to:
run gui.py to run the recommendation engine using 'python -i gui.py'
For Existing User
    - enter in username 'ohio64', or if you have an account, enter in your account name
    - Hit the no button, and then the login button
    - Adjust the weights using the + and - buttons (weights add up to 100)
    - Hit finish to get the top 10 shows
    - output will be in the terminal that ran gui.py
For New User
    - leave username blank, hit the yes button, then hit login
    - click on the 5 options to fill in your top 5 genres
    - asjust the weights using the + and - buttons (weights add up to 100)
    - hit finish and the top 10 shows will be outputted in the terminal
Output will take a little bit to be outputted

run Data_Visualization.py for data visualization of this recommendation system
- in Data_Visualization.py, replace the user variable with a string containing the username that you wish to test
- if jupyter notebook is preferable, the Data_Visualization.ipynb works as wells
