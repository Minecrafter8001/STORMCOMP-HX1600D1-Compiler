A simple compiler for the STORMCOMP HX1600D1 computer  
Compiler made by [me](https://steamcommunity.com/id/minecrafter8001/)  
Computer made by [MaxBuilder](https://steamcommunity.com/profiles/76561198145551187)

Clone the repo, put the compiler.py file in its own folder with an input.txt file that contains the assembly code for your program.  
run the compiler with a python interpreter and copy the two variable names from the output.txt file into the microcontroller (or manually enter them into the computer when it's spawned).  
AIRA is the instruction register.  
AIRB is the data register.

Instructions on how to use and program the computer are on its workshop page:  
https://steamcommunity.com/sharedfiles/filedetails/?id=3425013619

notes:
numbers at the start of a line are filtered out before compliation but are not required
lines starting with "--" are also ignored for comments
example:
"
--load 5 into accumulator
5 LD 5
SUB 2
" 
becomes:
"
LD 5
SUB 2
"


