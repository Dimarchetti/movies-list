# Search Movies on an API

This project has a study purpose. 
The main goal of this project is get all the informations of a movie on an API searching only for the name of the movie.

Development Language: Python

Python Libraries: requests and json

First step is define a function to get the request of an API to parse and show as a json response, making a Try-Exception to catch some error in the core of this function.

On the second step, a function to show all the relevant movie information is defined.

Following to the last step, an while is defined to get the input of the user with the movie name, giving the choice of exit of system. 
Into this while an if-else is defined to show the details of the movie, but if a movie is not found the else show the message "Movie not found" and the while give the input for entry a new movie name again for the user.

Movie details showed:

Name, Actors, Director(s), Awards, Released, Genre, IMDb Rating, and a poster image.
