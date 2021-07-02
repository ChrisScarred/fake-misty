# Fake Misty
This repository contains a simulation of Misty's REST and WebSockets API for Misty2py testing when a real Misty II is not available. Note that this module is only intended for testing the internal workings of the Misty2py package and is not suitable for any real-life testing.

## Usage

- `pip install poetry` to obtain Poetry
- `poetry install` to obtain the dependencies
- `poetry run python -m src.app` to run the simulated API
- fill in `127.0.0.1:5002` for Misty's IP address in `.env` file in Misty2py directory
- the unit tests defined in Misty2py run successfully if these instructions are followed
