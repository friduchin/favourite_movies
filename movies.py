import favourite_movies
from media import Movie

andalusian_dog_1929 = Movie('An Andalusian Dog',
                            'http://www.mir-dali.ru/images/andalus/afisha2.jpg',
                            'https://www.youtube.com/watch?v=R5K1ARvyvAc')

double_indemnity_1944 = Movie('Double Indemnity',
                              'https://st.kp.yandex.net/im/poster/2/5/4/kinopoisk.ru-Double-Indemnity-2549246.jpg',  # NOQA
                              'https://www.youtube.com/watch?v=yKrrAa2o9Eg')

becket_1964 = Movie('Becket',
                    'https://st.kp.yandex.net/im/poster/1/7/3/kinopoisk.ru-Becket-1735291.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=ArLJHj4WKYA')

day_of_jackal_1973 = Movie('The Day of the Jackal',
                           'https://st.kp.yandex.net/im/poster/1/3/2/kinopoisk.ru-The-Day-of-the-Jackal-1326257.jpg',  # NOQA
                           'https://www.youtube.com/watch?v=eMj5TpWuLf4')

star_1975 = Movie('The Captivating Star of Happiness',
                  'https://st.kp.yandex.net/im/poster/2/3/9/kinopoisk.ru-Zvezda-plenitelnogo-schastya-239156.jpg',  # NOQA
                  'https://www.youtube.com/watch?v=WVx_TPfoxFQ')

justice_for_all_1979 = Movie('...And Justice for All',
                             'https://st.kp.yandex.net/im/poster/1/7/0/kinopoisk.ru-And-Justice-for-All-1706557.jpg',  # NOQA
                             'https://www.youtube.com/watch?v=sQzYNoLANrg')

robocop_1987 = Movie('RoboCop',
                     'https://st.kp.yandex.net/im/poster/1/4/8/kinopoisk.ru-RoboCop-1482441.jpg',  # NOQA
                     'https://www.youtube.com/watch?v=zbCbwP6ibR4')

carlitos_way_1993 = Movie("Carlito's Way",
                          'https://st.kp.yandex.net/im/poster/2/1/3/kinopoisk.ru-Carlito_27s-Way-2136971.jpg',  # NOQA
                          'https://www.youtube.com/watch?v=0yehgqPtG3Y')

frida_2002 = Movie('Frida',
                   'http://st-im.kinopoisk.ru/im/poster/2/0/4/kinopoisk.ru-Frida-2045932.jpg',  # NOQA
                   'http://www.youtube.com/watch?v=uOUzQYqba4Y')

there_will_be_blood_2007 = Movie('There Will Be Blood',
                                 'https://st.kp.yandex.net/im/poster/1/3/3/kinopoisk.ru-There-Will-Be-Blood-1337593.jpg',  # NOQA
                                 'https://www.youtube.com/watch?v=FeSLPELpMeM')

outrage_2010 = Movie('Outrage',
                     'https://st.kp.yandex.net/im/poster/1/9/7/kinopoisk.ru-Autoreiji-1979526.jpg',  # NOQA
                     'https://www.youtube.com/watch?v=9pWRU0A0TbM')

super_2010 = Movie('Super',
                   'https://st.kp.yandex.net/im/poster/1/6/0/kinopoisk.ru-Super-1601272.jpg',  # NOQA
                   'https://www.youtube.com/watch?v=eL57ncw2jr8')

movies = [andalusian_dog_1929,
          double_indemnity_1944,
          becket_1964,
          day_of_jackal_1973,
          justice_for_all_1979,
          robocop_1987,
          carlitos_way_1993,
          there_will_be_blood_2007,
          frida_2002,
          super_2010,
          outrage_2010,
          star_1975]

favourite_movies.open_movies_page(movies)

