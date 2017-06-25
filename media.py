import webbrowser

'''This Docstring explains what the movie()class does'''
class Movie():
    '''This module will call for inputs of title, plot, poster, and trailer given by entertainment_center.py'''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''This module will call for the trailer of the movie to open in another window, as given by the import function webbrowser.'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
