from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Artur')
    director_2 = Director(id=2, name='Kate')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])
    director_dao.create = MagicMock(return_value=Director(id=3, name="Test"))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='comedy')
    genre_2 = Genre(id=2, name='action')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=Genre(id=3, name='documentary films'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='title1', description='description1', trailer='link1', year=2023, rating=7.7,
                    genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='title2', description='description2', trailer='link2', year=2022,
                    rating=7.6, genre_id=2, director_id=2)
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=Movie(id=3, title='title3', description='description3', trailer='link3',
                                                    year=2021, rating=7.5, genre_id=1, director_id=1))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
