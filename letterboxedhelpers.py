import sqlite3

con = sqlite3.connect("letterboxed")
cur = con.cursor()

def get_movie_info():
    movie_title = input("Enter a movie title: ").strip()

    cur.execute("""
    SELECT m.title, m.year, r.user_rating, r.date_rated, s.platform
    FROM ratings r
    JOIN movies m ON r.movie_id = m.movie_id
    LEFT JOIN sources s ON r.source_id = s.source_id
    WHERE LOWER(m.title) LIKE LOWER(?);
    """, (f"%{movie_title}%",))

    results = cur.fetchall()

    if not results:
        print(f"No matches found for '{movie_title}'.")
    else:
        print(f"\n Results for '{movie_title}':")
        for title, year, rating, date, platform in results:
            print(f" - {title} ({year}) → {rating}/5 on {date} [{platform or 'Unknown source'}]")

def get_movie_rating():
    rating = input("Show me movies I rated the same or higher than: ").strip()

    cur.execute("""
    SELECT m.title, m.year, r.user_rating
    FROM ratings r
    JOIN movies m ON r.movie_id = m.movie_id
    WHERE r.user_rating >= ?
    ORDER BY r.user_rating DESC
    """, (rating,))

    results = cur.fetchall()

    if not results:
        print(f"No matches found for ratings higher than '{rating}'.")
    else:
        print(f"\n Results for '{rating}':")
        for title, year, user_rating in results:
            print(f" - {title} ({year}) {user_rating}")