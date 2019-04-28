g2
-- 

![alt image](https://img.shields.io/badge/version-2.1.0-blue.svg) ![alt image](https://img.shields.io/badge/Python-3-blue.svg)

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
./g2 -dr 0 2 (Unregister directories from 0 to 2)
./g2 -spt ~/foo (save a directory to the top)
./g2 -m test (Jump to the first matched directory if you registered it ex. /foo/bar/test)
```

### Options
- -l --list:
	List all directories which you registered. If the path exists, it shows ✔️ else it shows 💀. 
- -lr --list-reversed:
	Reverse a list and show it.
- -s --save:
	Save a current directory.
- -sp --save-path [path]:
	Save a specified directory.
- -st --save-at-top:
    Save a current directory at the top(i.e. 0).
- -spt --save-path-at-top [path]:
	Save a specified directory at the top.
- -d --delete [num]:
	Unregister a saved directory with the number.
- -dr --delete-range [num1] [num2]:
	Unregister saved directories from num1 to num2.
- -c --change [num1] [num2]:
	Swap indexes which you specified.
- -m --match [string]:
    if a bottom of directory you registered contains a string, jump to the first matched directory.
    
### Tips
You can use g2 anywhere by aliasing in .bashrc 
```
alias g2='python3 path/to/g2'
```
### License
MIT

