def mod_sub(fun):
  def inner(a, b):
    if a < b:
      a, b = b, a
    fun(a, b)   

  return inner

@mod_sub
def div(a, b):
  print(a / b)

div(2, 4)
