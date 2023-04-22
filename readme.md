# Access

This repository contains two folders, `frontend` and `backend`, that respectively hold the Vue.js and Django components of an authentication system that works with Django APIs.

## Frontend

The `frontend` folder contains the Vue.js code for the user interface of the authentication system. To run the frontend, navigate to the `frontend` directory and run the following commands:

npm install
npm run serve


This will install the required dependencies and start the frontend server. The frontend can be accessed by visiting `http://localhost:8080` in your web browser.

## Backend

The `backend` folder contains the Django code for the authentication system's APIs. To run the backend, navigate to the `backend` directory and run the following commands:

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

This will install the required dependencies, migrate the database, and start the backend server. The backend APIs can be accessed by sending HTTP requests to `http://localhost:8000/api`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
# Access
