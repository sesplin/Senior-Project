# Senior-Project
Web application created with Python, HTML, CSS, and Vue.js

# Table of Contents
- General Info
- Technologies
- Setup

# General Info

# Technologies

# SQlite Schema

```sql
CREATE TABLE vacations(
id INTEGER PRIMARY KEY,
city TEXT,
state TEXT,
country TEXT,
site1 TEXT
site2 TEXT);
```

```sql
CREATE TABLE users(
userId INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT,
password TEXT );
```

# REST Endpoints


Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve vacation collection   | GET    | /vaca
Retrieve vacation member       | GET    | /vaca/*\<id\>*
Create vacation member         | POST   | /vaca
Create user member             | POST   | /users
Validate user member           | POST   | /sessions
Update vacation member         | PUT    | /vaca/*\<id\>*
Delete vacation member         | DELETE | /vaca/*\<id\>*
