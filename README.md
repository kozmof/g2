g2
-- 

![alt image](https://img.shields.io/badge/version-2.0.0-blue.svg) ![alt image](https://img.shields.io/badge/Python-3-blue.svg)

g2 makes you move to anywhere you registered in CLI.

**Currently Tested in:**
- Python 3.5.2, GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)

### Examples
```
./g2 (Jump to a directory numbered as 0)
./g2 -l (List all directories with numbers)
./g2 3 (Jump to a directory numbered as 3)
./g2 -c 1 5 (Swap saved directories numbered as 1 and 5 in a list)
./g2 -s (Save a current directory)
./g2 -dr 0 2 (delete directories from 0 to 2)
./g2 -spt ~/foo (save a directory to the top)
```

### Options
- -l --list:
	List all directories which you registered. If the path exists, it shows ✔️ else it shows 💀. 
- -lr --list-reversed:
	Reverse a list and show it.
- -s --save
	Save a current directory.
- -sp --save-path:
	Save a specified directory.
- -st --save-at-top:
    Save a current directory at the top(i.e. 0).
- -spt --save-path-at-top:
	Save a specified directory at the top.
- -d --delete [num]:
	Delete a saved directory with the number.
- -dr --delete-range [num1] [num2]:
	Delete saved directories from num1 to num2.
- -c --change [num1] [num2]:
	Swap indexes which you specified.
    
### Tips
You can use g2 anywhere by aliasing in .bashrc 
```
alias g2='python3 path/to/g2'
```
