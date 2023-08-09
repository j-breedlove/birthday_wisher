# Email Automation Script

This script provides functionality to send automated emails for different purposes, such as sending birthday wishes and weekly motivational quotes.

## Features

- Sends birthday emails to users whose birthdays match the current date.
- Sends a motivational quote every Monday.

## Setup

1. Clone the repository:

```
git clone <repository-url>
```

2. Navigate to the project directory:

```
cd <project-directory>
```

3. Install the required Python packages using Pipenv:

```
pipenv install
```

4. Activate the Pipenv shell:

```
pipenv shell
```

5. Set up your environment variables. Create a `.env` file in the root directory with the following content:

```
MY_EMAIL=<Your-Email>
PASSWORD=<Your-Email-Password>
```

**Note**: Be sure to keep your `.env` file secure and never commit it to the repository. `pipenv` will automatically pick up the variables from `.env` file when the script is run.

## Usage

To run the script:

```
python main.py
```

By default, the script will send a motivational quote. You can modify the `main` function call in the script to send birthday emails or extend the functionality.

## License

This project is licensed under the MIT License.
