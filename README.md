## g2
g2 makes you jump to directories which you registered.

Tested in:
Python 3.5.2
GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)

## Example
```
./g2 (Jump to a path numbered as 0)
./g2 3 (Jump to a path numbered as 3)
./g2 -c 1 5 (Swap paths numbered as 1 and 5)
./g2 -s (Save a new directory)
```

## Options
- -l --list
	List all directories which you registered.
- -lr --list-reversed
	Reverse a list and show it.
- -s --save
	Save a current directory.
- -d --delete num 
	Delete a directory with the number.
- -c --change num num
	Swap indexes which you spedified.
    
## Tips
You can use g2 anywhere by aliasing in .bashrc 
```
alias g2='python3 path/to/g2'
```