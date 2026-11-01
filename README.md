# TubeRadar

TubeRadar is a Python application that uses the Groq API to provide AI-powered functionality.

## Features

- Uses the Groq API for AI-powered responses.
- Loads API credentials securely using environment variables.
- Uses Python and the `python-dotenv` package for configuration.

## Requirements

- Python 3.9 or later
- A Groq API key
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/adyaa2102-hue/tube_radar
   ```

2. Open the project folder:

   ```bash
   cd tube_radar
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a file named `.env` in the project folder.

5. Add your Groq API key to the `.env` file:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Replace the placeholder with your own API key.

## Running the Application

Run the following command from the project folder:

```bash
python main.py
```

## API Key Security

- Never upload your real `.env` file to GitHub.
- The repository includes `.env.example` as a template.
- Keep your API key private.
- Each user should provide their own Groq API key.

## Project Structure

```text
tube_radar/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Dependencies

Install all required packages using:

```bash
python -m pip install -r requirements.txt
```

## License

This project is available for personal and educational use. Add a license file if you want to specify formal reuse and distribution permissions.



