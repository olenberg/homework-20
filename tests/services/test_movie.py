import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie = {
            "title": "test",
            "description": "test",
            "trailer": "test",
            "year": 2010,
            "rating": 7.3,
            "genre_id": 1,
            "director_id": 1
        }
        movie = self.movie_service.create(movie)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie = {
            "id": "1",
            "title": "test",
            "description": "test",
            "trailer": "test",
            "year": 2021,
            "rating": 8.9,
            "genre_id": 1,
            "director_id": 3
        }
        self.movie_service.update(movie)