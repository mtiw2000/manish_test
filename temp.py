# myname.py

def get_name():
    return "Jim"


def only_odd_mul(x, y):
   if x%2 and y%2:
       return x * y
   else:
       raise NoEvenNumbersHereException(f'{x} and/or {y} not odd')
       
 
def test_odd_numbers():
    assert only_odd_mul(3,5) == 15
    
      