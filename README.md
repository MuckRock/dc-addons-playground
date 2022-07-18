# dc-addons-playground

Experiments with [DocumentCloud addons](https://www.documentcloud.org/help/add-ons/).

# Setup

- Set up a virtual environment with `python3.9 -m venv venv`.
- Put `NLTK_DATA=nltk_data` in your `.env` file.
- Put your DocumentCloud credentials in `.env` as `USER` and `PASSWORD`. (Keep your `.env` safe.)
- Run `venv/bin/pip install -r requirements.text`.
- Run `make install-nltk`.

# Development

Try it out with `venv/bin/python summarize.py`.
