g2
===
![alt image](https://img.shields.io/badge/version-1.0.0-blue.svg) ![alt image](https://img.shields.io/badge/Python-3.5-blue.svg)

g2 makes you jump to anywhere you registered in CL.

**Currently Tested in:**
- Python 3.5.2 x GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)

## Examples
```
./g2 (Jump to a path numbered as 0)
./g2 -l (List all paths with numbers)
./g2 3 (Jump to a path numbered as 3)
./g2 -c 1 5 (Swap paths numbered as 1 and 5)
./g2 -s (Save a new path)
```

## Options
- -l --list:
	List all directories which you registered.
- -lr --list-reversed:
	Reverse a list and show it.
- -s --save:
	Save a current directory.
- -d --delete num:
	Delete a saved path with the number.
- -c --change num num:
	Swap indexes which you specified.
    
## Tips
You can use g2 anywhere by aliasing in .bashrc 
```
alias g2='python3 path/to/g2'
```
