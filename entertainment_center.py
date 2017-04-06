import media
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

nayagan.show_trailer()
