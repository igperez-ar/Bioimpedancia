# BioImp

BioImp is a Django-based web application for bioimpedance analysis and simulation. Bioimpedance is the phenomenon by which biological tissue opposes the passage of electrical current. Each tissue has different impedance characteristics, which allows distinguishing fat from lean mass, or air from water or bone.

This project contains the solution presented in the paper "Low cost Bioimpedance Applications: a solution to the csv files problem for the AD5933EB" published in the Argentine Journal of Bioengineering (SABI) - ISSN 2591-376X - Vol. 24 (4), 2020.

## Purpose

The project provides tools for:
- Bioimpedance measurement analysis
- Simulation of bioimpedance responses
- File management and processing of bioimpedance data
- Data visualization and reporting


## Features

- **Directory Management System**: Handles file uploads and organization of bioimpedance measurements
- **Bioimpedance Simulator**: Simulates tissue responses to electrical currents
- **File Processing**: 
  - Automatic CSV file repair and formatting
  - ZIP file generation for processed data
  - PDF report generation
- **Multi-language Support**: 
  - Primary language: Spanish (Argentina)
  - Configurable for English, Italian, and Portuguese (currently commented out)

## Technology Stack

- Python 3.x
- Django 2.2
- Bootstrap 3.x
- Additional Python packages:
  - fpdf: For PDF report generation
  - zipfile: For compressed file handling
  - csv: For data file processing

## Installation

1. Clone the repository

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the environment:
```bash
export DJANGO_SETTINGS_MODULE=bioimp.settings.dev  # For development
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

- `directory/`: Main application for file management and processing
- `simulador/`: Bioimpedance simulation module
- `settings/`: Configuration files
  - `dev.py`: Development settings
  - `prod.py`: Production settings
  - `settings.py`: Base settings

## File Processing

The application includes a file processing utility that:
- Repairs CSV files with incorrect formatting
- Standardizes data column separators
- Creates ZIP archives of processed files
- Generates formatted reports

## Configuration

The project uses Django's settings system with separate configurations for development and production environments. Key settings include:

- Time Zone: America/Buenos_Aires
- Language: Spanish (Argentina)
- Database: SQLite3 (default)
- Static/Media file configuration

## Static Files

The project uses various static files including:
- Bootstrap File Input plugin for enhanced file upload capabilities
- Font Awesome icons
- Custom CSS/JS files

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

The project uses various components with different licenses:
- Font Awesome: SIL OFL 1.1
- Bootstrap File Input: MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support or questions about bioimpedance analysis and simulation, please refer to the FAQ section in the application or open an issue in the project repository.

## Security Notes

For production deployment:
1. Change the SECRET_KEY
2. Set DEBUG = False
3. Configure specific ALLOWED_HOSTS
4. Set up proper security middleware
5. Configure a production-grade database

## Acknowledgments

- Django Software Foundation
- Bootstrap File Input by Kartik Visweswaran
- Font Awesome project
- All other open-source contributors
