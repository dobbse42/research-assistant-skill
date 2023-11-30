import nltk
nltk.download('punkt')

import pypdf
import arxiv_handler
from nltk.tokenize import sent_tokenize

class Paper:

  def __init__(self, id):
    print("init")
    self.page_starts = []
    self.language = 'en'
    self.link = 'placeholder'
    self.name = 'placeholder'
    self.arxiv_id = id
    self.filepath = arxiv_handler.get_arxiv(self.arxiv_id)
#    self.filepath = arxiv_handler.get_pdf(self.link)
    self.processed_sents = self.process_pdf(self.filepath)
#    self.processed_sents = process_text(self.raw_text)
    return

# Note: This does not handle sentences which begin on one page and end on the next. In that case the current behavior
#  is to split into two sentences, one part for each page.
  def process_pdf(self, filepath):
    path = open(filepath, 'rb')
    pdfReader = pypdf.PdfReader(path)
    texts = []
    text = ''
    sents = []
    for page in pdfReader.pages:
      texts.append(page.extract_text())
    for page in texts:
      self.page_starts.append(len(sents))
      sents = sents + self.process_text(page)
    return sents

  def process_text(self, text):
    text = text.replace('-\n', '') # handles word interrupt hyphens
    text = text.replace('\n', '') # remove newlines
    sents = sent_tokenize(text)
    return sents
