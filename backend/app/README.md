# E-commerce Backend

This is a Flask-based e-commerce backend application that utilizes SQLAlchemy for database management. The project is structured to provide a clear separation of concerns, making it easy to manage and extend.

## Project Structure

```
backend
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── controllers.py
│   └── config.py
├── requirements.txt
├── run.py
└── README.md
```




   pip install -r requirements.txt
   

 **Set up the database:**
   - Ensure you have a database set up as per the configuration in `app/config.py`.
   - Run the necessary migrations to create the database tables.

## Usage

To run the application, execute the following command:

```
python run.py
```

The application will start on `http://127.0.0.1:5000/`.

## Features

- User authentication and management
- Product catalog management
- Order processing and management
- RESTful API endpoints for frontend integration

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.