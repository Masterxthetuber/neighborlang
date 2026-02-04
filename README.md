*NeighborLang is a esolang based on brainfuck the syntax containa 10 features which can be seen in the list bellow*
* syntax
    - \> to move pointer right
    - < to move pointer left
    -  `+` to increment cell
    - `-` to decrement cell
    - ? to increment if previous cell which is one of the types of neighbor cells and the current cell are equal else decrement
    - / does the same as ? but if not equal
    - ; does the same as ? but to the next neighbor cell
    - \# to clear cell to zero
    - \* increments current cell by previous neighbor
    - & decrements current cell by previous neighbor
    - ^ increments current cell by next neighbor
    - % increments current cell by previous neighbor   
    - : does the same as / but for the next neighbor cell
    - if the operation is an int it will goto the index of the program element for example if you had lets say 3 your would go to the 4th element of program
    - r does a return countinuing to the next operation after the goto



