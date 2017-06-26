# Katie Sawicki's Movie Project 
## Introduction
The following python files are to serve as my submission for Udacity's "movie project." My submission contains the basic foundation of  _fresh_tomatoes.py_,  _media.py_ and _entertainment_center.py_. The function of this project is to display my favorite movies, the movie poster images, and when clicked on will display the movie's trailer. 

## Software/Equipment Needed 
* Python IDLE/ any Python reader
* Any web browser for the HTML file, "Fresh Tomatoes", to open within

## Bugs
(_There aren't any issues or bugs to report so far, unless the movies' poster images/trailer links are deleted, lead to 404, etc._)

## Technical
1. In order to create this project, you will need two separte modules (in this case, mine is media.py and entertainment center.py)
You can create these files (or customize the files I have provided) within your preferred Python IDLE. 
2. The code can be easily customized by following the basic setup for your module that will layout the Movie() structure (my case: media.py):
```
title_of_movie = media.Movie(
    self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
```

3. Within your second module (in this case, the entertainment_center.py module), follow along this basic
formula to submit up to 6 movie instances or beyond:
```
# Comment what the following movie will be

name_of_movie = media.Movie(Title,
                        "Description of the movie's plot",
                        "Link to movie's image",
                        "Link to Youtube trailer"
print (name_of_movie.storyline)
```

4. **Make sure all modules are within the same folder on your computer and that file names are lowercase (trust me, I
felt like an idiot trying to link the modules using a different case: "Media" vs "media")**

5. Remember to **import fresh_tomatoes** into the module of your instances of movies. 

6. Once you have followed the above steps and saved both modules - "run" the program: "entertainment_center.py."

To make sure the program has run properly, the generated HTML page should automatically pop up into your
preferred browser.

## License

MIT License

Copyright (c) [2017] [Udacity / Katherine Sawicki]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


