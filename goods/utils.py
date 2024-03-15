from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline


def q_search(query):
  '''Поиск по id и полнотекстовый поиск по названию и описанию'''
  if query.isdigit() and len(query) <= 5:
    return Products.objects.filter(id=int(query))

  vector = SearchVector("title", "description")
  query = SearchQuery(query)
  result = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

  result = result.annotate(headline=SearchHeadline("title", query, start_sel='<span style="background-color: yellow;">', stop_sel="</span>"))
  result = result.annotate(bodyline=SearchHeadline("description", query, start_sel='<span style="background-color: yellow;">', stop_sel="</span>"))

  return result

