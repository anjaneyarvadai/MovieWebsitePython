import media, fresh_tomatoes
#good to keep class definition in one file, and use it in other files
#similar to brad turtle example

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "Marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

nayagan = media.Movie("Nayagan",
                    "Story of Velu Naicker",
                    "https://upload.wikimedia.org/wikipedia/en/7/7b/Nayagan_poster.jpg",
                    "https://www.youtube.com/watch?v=mMXtoxdJdXk")

baasha = media.Movie("Baasha",
                    "Don who turns into autorickshaw driver",
                    "https://upload.wikimedia.org/wikipedia/en/6/6e/Baasha_Poster.jpg",
                    "https://www.youtube.com/watch?v=0lZ4Uf0ST9A")

fightclub = media.Movie("Fight Club",
                    "Personalities of Tyler Durden",
                    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

intothewild = media.Movie("Into The wild",
                    "College graduate goes on an Alaskan wilderness trip",
                    "https://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",
                    "https://www.youtube.com/watch?v=lwtZgBFKlzs")

movies = [toy_story, avatar, nayagan, baasha, fightclub, intothewild]
fresh_tomatoes.open_movies_page(movies)
