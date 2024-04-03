<!-- @format -->

# test_app_be

test_app_be/
│
├── app/
│ ├── **init**.py
│ ├── models.py
│ ├── schemas.py
│ ├── controllers/
│ │ ├── **init**.py
│ │ ├── auth.py
│ │ ├── posts.py
│ │ └── users.py
│ ├── services/
│ │ ├── **init**.py
│ │ ├── authentication.py
│ │ ├── post_service.py
│ │ └── user_service.py
│ └── main.py
│
├── tests/
│ ├── **init**.py
│ ├── test_auth.py
│ ├── test_posts.py
│ └── test_users.py
│
├── alembic/
│ ├── versions/
│ │ └── README
│ └── env.py
│
├── requirements.txt
└── README.md
