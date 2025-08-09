# Simple Calculator

A clean and simple calculator demo built with Python and Streamlit, following SOLID principles.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Clean and intuitive user interface
- Error handling for invalid operations
- Unit tests for all operations

## Project Structure

```
calculator/
├── src/
│   ├── __init__.py
│   ├── calculator.py      # Core calculator logic
│   └── app.py            # Streamlit interface
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jaimeman84/simple-calculator.git
cd simple-calculator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the calculator app:

```bash
streamlit run src/app.py
```

The application will open in your default web browser.

## Running Tests

To run the unit tests:

```bash
pytest tests/
```

## Design Principles

This calculator is built following SOLID principles:

- **Single Responsibility Principle**: Each class has one responsibility
- **Open/Closed Principle**: New operations can be added without modifying existing code
- **Liskov Substitution Principle**: All operation classes can be used interchangeably
- **Interface Segregation**: Operations are defined by a simple interface
- **Dependency Inversion**: High-level modules depend on abstractions

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 