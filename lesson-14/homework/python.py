# 1
import json

with open('students.json') as f:
    data = json.load(f)

for student in data['students']:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
# 2
import requests

API_KEY = 'your_api_key_here'
city = 'Tashkent'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(f"City: {city}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Weather: {data['weather'][0]['description']}")
# 3
import json

def load_books(file='books.json'):
    with open(file, 'r') as f:
        return json.load(f)

def save_books(books, file='books.json'):
    with open(file, 'w') as f:
        json.dump(books, f, indent=2)

def add_book(books, new_book):
    books['books'].append(new_book)

def update_book(books, title, updated_info):
    for book in books['books']:
        if book['title'] == title:
            book.update(updated_info)

def delete_book(books, title):
    books['books'] = [b for b in books['books'] if b['title'] != title]

# Example usage
books = load_books()
add_book(books, {'title': 'New Book', 'author': 'John Doe'})
update_book(books, 'Old Title', {'author': 'Updated Author'})
delete_book(books, 'Some Book')
save_books(books)
# 4
import requests
import random

API_KEY = 'your_omdb_api_key'
genre = input("Enter a movie genre (e.g., Action, Comedy): ")

# Example search query (OMDb API doesn't support full genre-based random lists in free tier)
url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"

response = requests.get(url)
data = response.json()

if 'Search' in data:
    movie = random.choice(data['Search'])
    print(f"Title: {movie['Title']}")
    print(f"Year: {movie['Year']}")
else:
    print("No movies found for that genre.")
