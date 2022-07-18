install-nltk:
	./venv/bin/pip install -U nltk && \
  mkdir -p venv/data && \
  NLTK_DATA=nltk_data ./venv/bin/python -m nltk.downloader punkt && \
  NLTK_DATA=nltk_data ./venv/bin/python -m nltk.downloader stopwords
