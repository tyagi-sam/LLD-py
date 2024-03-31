from Enums.City import City
from Enums.SeatCategory import SeatCategory
from booking import Booking
from movieController import MovieController
from theatreController import TheatreController
from movie import Movie
from theatre import Theatre
from show import Show
from screen import Screen
from seat import Seat


class BookMyShow:
    def __init__(self):
        self.movieController = MovieController()
        self.theatreController = TheatreController()

    def main(self):
        bookMyShow = BookMyShow()
        bookMyShow.initialize()

        # User1
        bookMyShow.createBooking(City.Bangalore, "BAAHUBALI")
        # User2
        bookMyShow.createBooking(City.Bangalore, "BAAHUBALI")
        # User 3
        bookMyShow.createBooking(City.Delhi, "IronMan")
        # User 4
        bookMyShow.createBooking(City.Delhi, "SpiderMan")

    def createBooking(self, userCity, movieName):
        movies = self.movieController.getMoviesByCity(userCity)
        interestedMovie = next((movie for movie in movies if movie.getMovieName() == movieName), None)

        if interestedMovie is None:
            print("Movie not found in the city")
            return

        showsTheatreWise = self.theatreController.getAllShow(interestedMovie, userCity)

        if not showsTheatreWise:
            print("No shows available for the movie in the city")
            return

        theatre, runningShows = next(iter(showsTheatreWise.items()))
        interestedShow = runningShows[0]

        seatNumber = 30
        bookedSeats = interestedShow.getBookedSeatIds()
        if seatNumber not in bookedSeats:
            bookedSeats.append(seatNumber)
            booking = Booking()
            myBookedSeats = [seat for seat in interestedShow.getScreen().getSeats() if seat.getSeatId() == seatNumber]
            booking.setBookedSeats(myBookedSeats)
            booking.setShow(interestedShow)
        else:
            print("Seat already booked, try again")
            return

        print("BOOKING SUCCESSFUL")

    def initialize(self):
        self.createMovies()
        self.createTheatre()

    def createTheatre(self):
        avengerMovie = self.movieController.getMovieByName("AVENGERS")
        baahubali = self.movieController.getMovieByName("BAAHUBALI")
        spiderman = self.movieController.getMovieByName("SpiderMan")

        inoxTheatre = Theatre()
        inoxTheatre.setTheatreId(1)
        inoxTheatre.setScreen(self.createScreen())
        inoxTheatre.setCity(City.Bangalore)
        inoxShows = [
            self.createShows(1, inoxTheatre.getScreen()[0], avengerMovie, 8),
            self.createShows(2, inoxTheatre.getScreen()[0], baahubali, 16)
        ]
        inoxTheatre.setShows(inoxShows)

        pvrTheatre = Theatre()
        pvrTheatre.setTheatreId(2)
        pvrTheatre.setScreen(self.createScreen())
        pvrTheatre.setCity(City.Delhi)
        pvrShows = [
            self.createShows(3, pvrTheatre.getScreen()[0], avengerMovie, 13),
            self.createShows(4, pvrTheatre.getScreen()[0], baahubali, 20),
            self.createShows(5, pvrTheatre.getScreen()[0], spiderman, 25)
        ]
        pvrTheatre.setShows(pvrShows)

        self.theatreController.addTheatre(inoxTheatre, City.Bangalore)
        self.theatreController.addTheatre(pvrTheatre, City.Delhi)

    def createScreen(self):
        screens = []
        screen1 = Screen()
        screen1.setScreenId(1)
        screen1.setSeats(self.createSeats())
        screens.append(screen1)
        return screens

    def createShows(self, showId, screen, movie, showStartTime):
        show = Show()
        show.setShowId(showId)
        show.setScreen(screen)
        show.setMovie(movie)
        show.setShowStartTime(showStartTime)
        return show

    def createSeats(self):
        seats = []
        for i in range(1, 41):
            seat = Seat()
            seat.setSeatId(i)
            seat.setSeatCategory(SeatCategory.SILVER)
            seats.append(seat)
        for i in range(41, 71):
            seat = Seat()
            seat.setSeatId(i)
            seat.setSeatCategory(SeatCategory.GOLD)
            seats.append(seat)
        for i in range(71, 101):
            seat = Seat()
            seat.setSeatId(i)
            seat.setSeatCategory(SeatCategory.PLATINUM)
            seats.append(seat)
        return seats

    def createMovies(self):
        avengers = Movie()
        avengers.setMovieId(1)
        avengers.setMovieName("AVENGERS")
        avengers.setMovieDuration(128)

        baahubali = Movie()
        baahubali.setMovieId(2)
        baahubali.setMovieName("BAAHUBALI")
        baahubali.setMovieDuration(180)

        spiderman = Movie()
        spiderman.setMovieId(3)
        spiderman.setMovieName("SpiderMan")
        spiderman.setMovieDuration(175)

        self.movieController.addMovie(avengers, City.Bangalore)
        self.movieController.addMovie(avengers, City.Delhi)
        self.movieController.addMovie(baahubali, City.Bangalore)
        self.movieController.addMovie(baahubali, City.Delhi)
        self.movieController.addMovie(spiderman, City.Delhi)

# Entry point
if __name__ == "__main__":
    bookMyShow = BookMyShow()
    bookMyShow.main()
