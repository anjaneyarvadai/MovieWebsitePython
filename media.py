import webbrowser

class Movie():
  #Google style guide for python suggests capital letter for Class names
  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    #self is object being created = constructor
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self):
    #instance method
    webbrowser.open(self.trailer_youtube_url)
