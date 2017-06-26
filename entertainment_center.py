import fresh_tomatoes
import media

# 1st movie instance

kill_bill = media.Movie("Kill Bill: Volume 1",
                        "A female ex-assassin chases "
                        "down the people reponsible for her "
                        "coma and unborn baby's death "
                        "ultimately to slay her lover that "
                        "betrayed her:Bill.",
                        "https://s-media-cache-ak0.pinimg.com/736x/ec/03/6f/ec036fda777280d0e1ea1067391157f7.jpg",  # NOQA
                        "https://youtu.be/ot6C1ZKyiME")
print (kill_bill.storyline)

# 2nd movie instance

the_help = media.Movie("The Help",
                       "In 1965, a southern white journalist "
                       "writes more than she expects "
                       "when she interviews black maids as "
                       "they tell their stories about "
                       "being 'the help' "
                       "in Jackson, Mississippi.",
                       "http://img.moviepostershop.com/the-help-movie-poster-2011-1020701031.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=l0dWCXCjX9o")

print(the_help.storyline)

# 3rd movie instance

howls_moving_castle = media.Movie("Howl's Moving Castle",
                                  "An ordinary girl is swept away into "
                                  "adventure when she is cursed "
                                  "by an evil witch. "
                                  "The only way to cure her is "
                                  "to travel with an amazing wizard "
                                  "named Howl and his enormous, "
                                  "enchanted castle.",
                                  "http://www.nausicaa.net/miyazaki/howl/poster_images/USA_full.jpg",  # NOQA
                                  "https://youtu.be/iwROgK94zcM")
print (howls_moving_castle.storyline)

# 4th movie instance

walle = media.Movie("WALL-E",
                    "After one hundred lonely "
                    "years after Earth has been "
                    "abandoned, a robot finds love "
                    "and is swept across the galaxy "
                    "with precious cargo: the last "
                    "remaining plant life.",
                    "http://www.impawards.com/2008/posters/wall_e.jpg",  # NOQA
                    "https://youtu.be/alIq_wG9FNk")

print(walle.storyline)

# 5th movie instance

memoirs_geisha = media.Movie("Memoirs of a Geisha",
                            "An ancient japanese tradition "
                             "becomes a gateway to happiness "
                             "and love for Chio, a budding geisha "
                             "with blue eyes. Within this world "
                             "of beauty, there is betrayl, "
                             "jealousy, and malicious acts that "
                             "can potentially destroy her "
                             "career, but Chio hopes to rise "
                             "above it all.",
                             "http://www.impawards.com/2005/posters/memoirs_of_a_geisha.jpg",  # NOQA
                             "https://youtu.be/EWRkt6hBVVc")
print (memoirs_geisha.storyline)

# 6th movie instance

deadpool = media.Movie("Deadpool",
                       "An anti-hero contracts a terminal "
                       "illness and entrusts that he will "
                       "be cured by a mysterious organization. "
                       "When he escapes from their malicious "
                       "maltreatment, he goes on a "
                       "rampage to extract revenge and "
                       "cure the side effects of the "
                       "experiments conducted on him.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")
print (deadpool.storyline)

movies = (kill_bill, the_help, howls_moving_castle,
          walle, memoirs_geisha, deadpool)
fresh_tomatoes.open_movies_page(movies)
