Match = { (1,3) , (2 ,3) , (3,3) , (4 ,5) , (5 ,10) , (6,2) , (7,9)}

Sets = set()
data = []
tuple = ()
Sets2 = set()

Tuple_win = ()
Tuple_loss = ()

Window_Sets = set()

for pair in Match:
    Tuple_win = Tuple_win + (pair[0],)
    Tuple_loss = Tuple_loss + (pair[1],)

Window_Sets.add(Tuple_win)
Window_Sets.add(Tuple_loss)

print(Window_Sets)