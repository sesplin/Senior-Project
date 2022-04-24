# Senior-Project
Web application to solve a problem involving credit card points

## Table of Contents
- Problem
- Solution
- Technologies
- SQlite Schema
- REST Endpoints

## Problem
Intelligent credit card users with multiple cards regularly have difficulty deciding what card to use when purchasing different items. This is due to the fact that they desire to purchase with the card that will provide them with the most reward points.

## Solution
A web application that will inform users who desire to maximize credit card reward points with individual purchases based on the credit cards that they currently own. It will provide individualized results which the user will indicate.

## Technologies
- Python
- HTML
- CSS
- Vue.js

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
