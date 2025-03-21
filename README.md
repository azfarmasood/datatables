# DataTables Scraper

A Python tool that scrapes and analyzes employee data from DataTables demo pages. This project demonstrates web scraping, data cleaning, and analysis capabilities using Python.

## Features

- 🌐 Scrapes employee data from DataTables demo pages
- 🧹 Cleans and processes the raw data
- 📊 Performs statistical analysis on employee data
- 💾 Saves both raw and cleaned data to CSV files
- 📈 Provides detailed salary and age statistics
- 🏢 Shows employee distribution by office

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd datatables
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

1. Activate the Poetry virtual environment:
```bash
poetry shell
```

2. Run the main script:
```bash
python -m datatables.app.main
```

The script will:
- Fetch data from the DataTables demo page
- Process and clean the data
- Generate analysis
- Save results to CSV files in the `app/data/csv` directory

## Project Structure

```
datatables/
├── datatables/
│   ├── __init__.py
│   └── app/
│       ├── controllers/
│       │   ├── cleaning_data.py
│       │   ├── data_analysis.py
│       │   ├── extract_data_from_tables.py
│       │   ├── save_to_csv.py
│       │   └── scrap_tables_data.py
│       ├── models/
│       │   └── analyse_data_models.py
│       └── main.py
├── pyproject.toml
└── README.md
```

## Dependencies

The project uses the following main dependencies:
- BeautifulSoup4 for web scraping
- Pandas for data manipulation
- Requests for HTTP requests
- Typing for type hints

All dependencies are managed through Poetry and specified in `pyproject.toml`.

## Output

The script generates two CSV files:
- `employee_data_raw.csv`: Raw data as scraped from the website
- `employee_data_clean.csv`: Cleaned and processed data

The analysis output includes:
- Total number of employees
- Salary statistics (min, max, mean, median)
- Age statistics (min, max, mean, median)
- Employee distribution by office

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Authors

- Afnan Siddiqui and Azfar Masood

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- DataTables for providing the demo data
- All contributors who have helped with the project
