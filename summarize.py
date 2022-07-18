from documentcloud import DocumentCloud
import os
from dotenv import load_dotenv
import heapq

load_dotenv()
print('NLTK_DATA', os.environ['NLTK_DATA'])
# .env needs to be loaded before importing nltk so that it knows
# where to look for data.
import nltk

max_docs_to_summarize = 2
docs_summarized = 0
stopwords = nltk.corpus.stopwords.words('english')

# TODO: Break this out so it can be used by an add-on that will
# summarize a single doc.
# https://stackabuse.com/text-summarization-with-nltk-in-python/
def summarize(doc, doc_count):
  if doc_count >= max_docs_to_summarize:
    return

  sentence_list = nltk.sent_tokenize(doc.full_text)

  word_frequencies = {}
  for word in nltk.word_tokenize(doc.full_text):
    if word not in stopwords:
      if word not in word_frequencies.keys():
        word_frequencies[word] = 1
      else:
        word_frequencies[word] += 1

  maximum_frequency = max(word_frequencies.values())

  for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

  sentence_scores = {}
  for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
      if word in word_frequencies.keys():
        if len(sent.split(' ')) < 30:
          if sent not in sentence_scores.keys():
            sentence_scores[sent] = word_frequencies[word]
          else:
            sentence_scores[sent] += word_frequencies[word]

  summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
  summary = ' '.join(summary_sentences)

  print('Summary for', doc.title)
  print(summary)

  doc_count += 1

user = os.environ['USER']
password = os.environ['PASSWORD']
client = DocumentCloud(user, password)

print(client.documents.list())

for doc in client.documents.list(): summarize(doc, docs_summarized)
