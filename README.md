# Superhero API

# By Leo Muraya Ngume

## Description

The Superhero API is a Flask-based backend that manages superheroes, their powers, and their strength levels. It provides endpoints for retrieving and modifying heroes, powers, and their relationships.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- SQLAlchemy Serializer
- Postman (for testing)

---

## Installation

### Clone the repository

```bash
$ git clone <repository_url>
$ cd <repository_name>
```

### Set up virtual environment

```bash
$ pipenv install
$ pipenv shell
```

### Initialize the database

```bash
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
```

### Seed the database

```bash
$ python seed.py
```

### Run the application

```bash
$ flask run
```

---

## API Endpoints

### Heroes

#### Get all heroes
```http
GET /heroes
```
Response:
```json
[
  {"id": 1, "name": "Spider-Man", "super_name": "Peter Parker"},
  {"id": 2, "name": "Iron Man", "super_name": "Tony Stark"}
]
```

#### Get a specific hero
```http
GET /heroes/:id
```
Response:
```json
{
  "id": 1,
  "name": "Spider-Man",
  "super_name": "Peter Parker",
  "hero_powers": [
    {"power": "Web-Slinging", "strength": "Strong"}
  ]
}
```

### Powers

#### Get all powers
```http
GET /powers
```
Response:
```json
[
  {"id": 1, "name": "Super Strength"},
  {"id": 2, "name": "Flight"}
]
```

#### Get a specific power
```http
GET /powers/:id
```
Response:
```json
{
  "id": 1,
  "name": "Super Strength",
  "description": "The ability to exert incredible physical force."
}
```

#### Update power description
```http
PATCH /powers/:id
```
Request:
```json
{
  "description": "New description for the power."
}
```
Response:
```json
{
  "id": 1,
  "name": "Super Strength",
  "description": "New description for the power."
}
```

### Hero Powers

#### Assign power to a hero
```http
POST /hero_powers
```
Request:
```json
{
  "hero_id": 1,
  "power_id": 2,
  "strength": "Strong"
}
```
Response:
```json
{
  "id": 1,
  "hero_id": 1,
  "power_id": 2,
  "strength": "Strong"
}
```

---

## Testing with Postman

1. Open Postman and create a new request.
2. Enter the API endpoint (e.g., `http://127.0.0.1:5000/heroes`).
3. Select the request method (GET, POST, PATCH, etc.).
4. If required, add JSON data under the "Body" tab and select "raw" > "JSON".
5. Click "Send" to make the request and check the response.

---

## License

This project is licensed under the MIT License.

