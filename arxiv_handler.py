import arxiv

def get_arxiv(my_id):
#  paper = next(arxiv.Client().results(arxiv.Search(id_list = ["2107.09200"])))
  paper = next(arxiv.Client().results(arxiv.Search(id_list = [my_id])))
  my_filename = paper.get_short_id() + '_' + paper.title.replace(' ', '_') + '.pdf'
  paper.download_pdf(filename = my_filename)
  return my_filename

# general method for downloading pdfs (i.e. non-arxiv material)
def get_pdf(url):
  filename = 'placeholder'
  return filename
