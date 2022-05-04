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
Create user member             | POST   | /users
Validate user member           | POST   | /sessions
![Mainpage](https://user-images.githubusercontent.com/70726533/166820696-95627212-0e63-4a8c-a277-a7201257823c.jpg)


![dropdown](https://user-images.githubusercontent.com/70726533/166820732-17ed8955-7409-4484-8511-eafbd9b6fb98.jpg)

![ProfilePage](https://user-images.githubusercontent.com/70726533/166820755-6a972f31-f0e6-407e-9fd3-cf9b59fc2630.jpg)



