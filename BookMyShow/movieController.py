from Enums.City import City
from movie import Movie

class MovieController:
    def __init__(self):
        self.cityVsMovies = {}
        self.allMovies = []

    def addMovie(self, movie: Movie, city: City):
        self.allMovies.append(movie)
        movies = self.cityVsMovies.get(city, [])
        movies.append(movie)
        self.cityVsMovies[city] = movies

    def getMovieByName(self, movieName):
        for movie in self.allMovies:
            if movie.getMovieName() == movieName:
                return movie
        return None

    def getMoviesByCity(self, city: City):
        return self.cityVsMovies.get(city, [])

    # Other CRUD operations such as remove movie from a particular city, update movie of a particular city,
    # and CRUD operations based on Movie ID can be added here as needed
