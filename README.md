# Trading Journal

A desktop trading journal developed as a learning project to practice software development, database integration, GUI development, data analysis, and application architecture using Python.

The application is designed to register, manage, and analyze trading operations while gradually incorporating statistics, charts, dashboards, and reporting features.

## Purpose

This project was created for learning and portfolio purposes.

The main goal is to apply programming concepts in a practical project while gaining experience with technologies commonly used in software development and data analysis.

## Features

Current and planned features include:

- Add trades
- Edit trades
- Remove trades
- Store trades locally
- Trade history
- Trade descriptions and notes
- Calendar-based trade visualization
- Performance metrics
- Trading statistics
- Dashboard
- Charts and data visualization
- Report generation

## Technologies

### Current

- Python
- PySide6
- Qt Designer
- SQLite
- SQLAlchemy
- Git
- GitHub

### Planned

- Pandas
- Matplotlib
- Power BI

Pandas will be used for data processing and analysis, while Matplotlib will be used for charts and statistics inside the application.

Power BI may later be used to create external reports and dashboards based on exported trading data.

## Project Structure

```text
TradingJournal/
├── database/
├── domain/
├── pages/
├── repositories/
├── ui/
├── main.py
├── .gitignore
└── README.md

The project follows a modular structure to separate responsibilities such as:
- user interface
- database access
- domain objects
- repository logic
- page-specific application logic

Database

Trades are stored locally using SQLite.
SQLAlchemy is used as the ORM layer to manage database models, queries, inserts, updates, and deletions.

Data Analysis

Future versions of the project will use Pandas to process trading data and calculate metrics such as:
- win rate
- profit and loss
- average results
- trades per day
- weekly and monthly performance
- performance by trade direction

These results can later be displayed inside the application using Matplotlib.
Future Development

Planned improvements include:
- complete trade editing
- trade deletion
- dashboard implementation
- calendar view
- performance analytics
- charts with Matplotlib
- data processing with Pandas
- report export
- Power BI integration
- additional validation and error handling

Status

This project is currently under development.
Features and architecture may change as new concepts and technologies are studied and implemented.

Disclaimer

This application is developed for learning and portfolio purposes only.
It is not intended to provide financial advice or be used as a professional trading platform.