# Senior-Project
Web application created with Python, HTML, CSS, and Vue.js

## Table of Contents
- General Info
- Technologies
- Setup

## Problem


## Solution

## Technologies

## SQlite Schema

```sql
CREATE TABLE users(
user_id INTEGER PR IMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
salted_pass TEXT NOT NULL,
current_points INTEGER);
```

```sql
CREATE TABLE cards(
card_id INTEGER PRIMARY KEY,
card_name TEXT NOT NULL,
company TEXT NOT NULL,
Travel INTEGER,
dining INTEGER,
groceries INTEGER,
fuel INTEGER,
shopping INTEGER);
```

```sql
CREATE TABLE usercards(
user_id INTEGER, 
card_id INTEGER);
```

## REST Endpoints


Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve card collection       | GET    | /cards
Retrieve user card collection  | GET    | /usercards
Retrieve user member           | GET    | /user/*\<name\>*
Retrieve user card collection  | GET    | /cards/travel
Retrieve user card collection  | GET    | /cards/dining
Retrieve user card collection  | GET    | /cards/grocery
Retrieve user card collection  | GET    | /cards/gas
Retrieve user card collection  | GET    | /cards/shopping
Create vacation member         | POST   | /vaca
Create user member             | POST   | /users
Validate user member           | POST   | /sessions
Update vacation member         | PUT    | /vaca/*\<id\>*
Delete vacation member         | DELETE | /vaca/*\<id\>*
