def count_deaf_rats(town):
    return town.replace(' ', '')[::2]


print(count_deaf_rats("~O~O~O~OP~O~OO~"))