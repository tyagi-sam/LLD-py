from Enums.City import City
from theatre import Theatre
from movie import Movie


class TheatreController:
    def __init__(self):
        self.cityVsTheatre = {}
        self.allTheatre = []

    def addTheatre(self, theatre: Theatre, city: City):
        self.allTheatre.append(theatre)
        theatres = self.cityVsTheatre.get(city, [])
        theatres.append(theatre)
        self.cityVsTheatre[city] = theatres

    def getAllShow(self, movie: Movie, city: City):
        theatreVsShows = {}

        theatres = self.cityVsTheatre.get(city, [])
        for theatre in theatres:
            givenMovieShows = []
            shows = theatre.getShows()

            for show in shows:
                if show.getMovie().getMovieId() == movie.getMovieId():
                    givenMovieShows.append(show)

            if givenMovieShows:
                theatreVsShows[theatre] = givenMovieShows

        return theatreVsShows
