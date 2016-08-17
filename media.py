class Movie():
    """Represents a movie object, containing some useful information
     (title, poster image URL and Youtube trailer URL)

    Attributes:
        title: A string with a movie title.
        poster_image_url: A string containing poster URL of the movie
        trailer_youtube_url: A string containing Youtube trailer link of the
            movie
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Init a movie object"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
