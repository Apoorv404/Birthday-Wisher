# Birthday-Wisher

An automated Python application that sends personalized birthday wishes via email to your friends and family on their special day!

## Description

Birthday-Wisher automatically checks a database of birthdays daily and sends personalized email greetings using randomly selected letter templates. Never forget to wish your loved ones on their birthday again!

## Features

- Automatic birthday checking
- Personalized email sending
- Multiple letter templates for variety
- CSV-based birthday database
- SMTP email integration
- Random template selection

## Project Structure

```
Birthday-Wisher/
├── birthdays.csv
├── main.py
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── README.md
```

## Requirements

- Python 3.x
- pandas library
- Access to an email account (Gmail recommended)
- SMTP server access

## Setup

1. Clone the repository
2. Install required package:
   ```
   pip install pandas
   ```
3. Update `birthdays.csv` with birthday information:
   - name
   - email
   - year
   - month
   - day

4. Configure email settings in `main.py`:
   - Set your email address
   - Set your email password/app password

## Usage

1. Add birthday entries to `birthdays.csv`
2. Run the script:
   ```
   python main.py
   ```
3. The script will:
   - Check for birthdays on the current date
   - Select a random template
   - Send personalized emails to anyone whose birthday matches today's date

## Note

- For Gmail users: You'll need to use an App Password instead of your regular password
- The script can be automated to run daily using task scheduler (Windows) or cron jobs (Linux/Mac)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
