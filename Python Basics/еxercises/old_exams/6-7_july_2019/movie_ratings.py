from sys import maxsize

number_of_movies = int(input())

min_rating = maxsize
max_rating = - maxsize
max_rating_movie_name = ''
min_rating_movie_name = ''
total_sum_of_ratings = 0

for movie in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_sum_of_ratings += movie_rating

    if movie_rating < min_rating:
        min_rating = movie_rating
        min_rating_movie_name = movie_name

    if max_rating < movie_rating:
        max_rating = movie_rating
        max_rating_movie_name = movie_name

print(f'{max_rating_movie_name} is with highest rating: {max_rating:.1f}')
print(f'{min_rating_movie_name} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {total_sum_of_ratings / number_of_movies:.1f}')