# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> * `pwd` - show current working directory path
>> * `mkdir` - creating a directory
>> * `rm -r` - deleting a directory
>> * `touch filename` - creating a file
>> * `rm` - deleting a file
>> * `mv old_name new_name` - renaming a file
>> * `ls -a` - listing hidden files
>> * `cp filename directory` - copying file from one directory to another
>> * `cd` - change directories
>> * `..` shorthand for moving up one directory

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> * `ls` - lists files in directory
>> * `ls -a` - lists all files in directory (even hidden ones!)
>> * `ls -l` - displays long format for files in directory
>> * `ls -lh` - the same thing as `ls -l`
>> * `ls -lah` - displayes long format for all files in directory (including hidden ones)
>> * `ls -t` - orders files in directory by date created
>> * `ls -Glp` - lists long format for files and subdirectories in directory, directories are highlighted and end with '/'

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> * `ls -1` - lists every item on own line
>> * `ls -m` - list displayed as comma separated list
>> * `ls -u` - list files by access time
>> * `ls -R` - lists subdirectories as well
>> * `ls -x` - displays items in directory as rows

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> `xargs` lets you build and execute statements by converting standard inputs into commands. It is especially helpful when
combined with other commands, for example:

>> ```bash
find . -name "*.json" | xargs rm -rf
```
 >> The above command would find all files with a .json extension in your current directory and remove them

 

