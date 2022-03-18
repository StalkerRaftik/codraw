import csv
import logging
import traceback
from datetime import datetime

import requests
from django.core.files.base import File
from django.core.management.base import BaseCommand
from django.db import transaction

from codraw.models.anime import Anime, AnimeStatus, Genre

# .csv header:
# ['uid', 'title', 'synopsis', 'genre', 'aired', 'episodes',
# 'members', 'popularity', 'ranked', 'score', 'img_url', 'link']


class Command(BaseCommand):
    help = 'Loads anime data from csv file.'
    genres = dict()

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['filenames']:
            with open(path, newline='') as csvfile:
                spamreader = csv.reader(csvfile)
                next(spamreader, None)  # skip header
                for row in spamreader:
                    try:
                        self.load_anime(row)
                    except Exception as e:
                        logging.error(traceback.format_exc())
                        print('An exception during anime loading occurred: {}'.format(e))

    @transaction.atomic
    def load_anime(self, row):
        episodes_count = int(float(row[5])) if row[5] else ''
        anime_data = {
            'original_name': row[1],
            'premiere_date': self.get_date(row[4]),
            'status': AnimeStatus.RELEASED,
            'added_episodes': episodes_count,
            'episodes_count': episodes_count,
            'description': row[2],
            'raw_rating': row[9],
            'raw_visits': row[6],
        }
        anime = Anime(**dict(filter(
            lambda item: bool(item[1]),
            anime_data.items()
        )))
        img_path = self.get_img(row[10])
        with open(img_path, 'rb') as f:
            anime.image.save(img_path, File(f), save=False)
        anime.save()

        genres_list = list(map(
            lambda genre_name: genre_name.strip(),
            row[3][1:-1].replace('\'', '').split(',')
        ))
        anime.genres.add(*self.get_genre_objects(genres_list))

    def get_genre_objects(self, genres_list):
        genres = []
        for genre_name in genres_list:
            genre = self.genres.get(genre_name)
            if genre:
                genres.append(genre)
                continue

            genre = Genre.objects.get_or_create(name=genre_name)[0]
            self.genres[genre_name] = genre
            genres.append(genre)

        return genres

    @staticmethod
    def get_date(raw_date):
        date_to_parse = raw_date.split('to')[0].strip().replace(',', '')
        return datetime.strptime(date_to_parse, '%b %d %Y')

    @staticmethod
    def get_img(url):
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            return

        path = f'images/anime/{url.split("/")[-1]}'
        with open(path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return path
