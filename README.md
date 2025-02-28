# A Simple Compiler for the STORMCOMP HX1600D1 Computer

**Compiler made by [me](https://steamcommunity.com/id/minecrafter8001/)**  
**Computer made by [MaxBuilder](https://steamcommunity.com/profiles/76561198145551187)**

Clone the repo, put the `compiler.py` file in its own folder with an `input.txt` file that contains the assembly code for your program. Run the compiler with a Python interpreter and copy the two variable names from the `output.txt` file into the microcontroller (or manually enter them into the computer when it's spawned).  
AIRA is the instruction register.  
AIRB is the data register.

Instructions on how to use and program the computer are on its [workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3425013619).

### Notes:
- **Numbers at the start of a line** are filtered out before compilation but are not required.
- **Lines starting with "`--`"** are also ignored as comments.

#### Example:
```plaintext
--load 5 into accumulator
5 LD 5
SUB 2
```
Becomes:
```plaintext
LD 5
SUB 2
```
To the compiler
