from documentcloud import DocumentCloud
import os
from dotenv import load_dotenv
import spacy
import pytextrank

max_docs_to_summarize = 2
docs_summarized = 0

nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")

def summarize(doc, doc_count):
  if doc_count >= max_docs_to_summarize:
    return

  summary_doc = nlp(doc.full_text)
  print('Summary for', doc.title)

  # examine the top-ranked phrases in the summary_document
  for phrase in summary_doc._.phrases:
      print(phrase.text)
      print(phrase.rank, phrase.count)
      print(phrase.chunks)
      doc_count += 1

load_dotenv()
user = os.environ['USER']
password = os.environ['PASSWORD']
client = DocumentCloud(user, password)

print(client.documents.list())

for doc in client.documents.list(): summarize(doc, docs_summarized)
