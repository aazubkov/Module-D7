from django import template


class MatError(Exception):
   pass


register = template.Library()
MAT_WORDS = ['спартак', 'индекс', 'мишустин', 'ввп', 'газпром']


@register.filter()
def correct_text(text=str):
   try:
      if type(text) != str:
         raise MatError
   except MatError:
      return ('Type Error')
   else:
      res = []
      for t in text.split():
         res.append(correct_word(t))
      res = ' '.join(res)
   return res


def correct_word(word):
   mat_flag = False
   res = word
   for mat in MAT_WORDS:
      if mat in word.lower():
         mat_flag = True
   if mat_flag:
      res = word[0] + '*' * (len(word) - 1)
   return res


