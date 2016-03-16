An example of classic data structures

David's check_parens:
    I started out trying to just count the number of each parentheses but of course that did not keep
    track if they fit together or not in an appropriate fasion. So then I started collecting them,
    in groups into a list and that did not work either. So I kept all the open ones in a list
    and tried removing them as list[-1] in a while loop and I kept getting stuck in the loop. I then
    remembered the pop method and using that as a base came up with my solution. I am not entirely
    sure if it is a true stack since the data is kept in a list, but it is a data structure
    where you put things in one way and take them out the same way. So it is close. I also included
    my tests and used the tox file already in our data-structure repo for the test.