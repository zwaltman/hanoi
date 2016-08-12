# hanoi
Implementation of recursive solution to the Tower of Hanoi problem using Python

From Wikipedia:

  "The Tower of Hanoi [...] is a mathematical game or puzzle. It consists of three 
  rods, and a number of disks of different sizes which can slide onto any rod. The 
  puzzle starts with the disks in a neat stack in ascending order of size on one 
  rod, the smallest at the top, thus making a conical shape.
  The objective of the puzzle is to move the entire stack to another rod, obeying 
  the following simple rules:
  1) Only one disk can be moved at a time.
  2) Each move consists of taking the upper disk from one of the stacks and placing it 
  on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
  3) No disk may be placed on top of a smaller disk."

This implementation of the Tower of Hanoi problem models the 3 poles as 3 lists
(treated as stacks), and models the disks as the elements in those lists. The 
size of the disks relative to one another is represented by the original ordering
of the items in the list they are being moved from. (They are ordered 'largest'-
to-'smallest' from left to right.) In this model the given algorithm follows all 
constraints of the problem.
