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

> > pwd, mkdir, rmdir, touch smth.txt, rm smth.txt, mv smth.txt smth1.txt,ls -ad .*, cp smth.txt ../temp/smth.txt

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

> > ls: lists all files in a directory, ls -a: displays files including those starting with ".", ls -l: displays long listing format of files/directories, ls -lh:same as ls -l except file size units are defined, ls -lah: displays all files in human readable format including files with ".",ls -t: list files/directory by date (most recent first), ls -Glp: lists content in long format with colouring of directories, -p indicating if output is a file or a directory.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -ltr, ls -1, ls -A, ls -S, ls -i

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Xargs, takes all the lines from the standard input and then concanates these arguments into a new set of inputs and executes this new command.  Such that the following example if $ find *.txt was piped directly to cksum, only one ouput would be returned which would be the addition of all the files with extension .txt. in the directory.  However, if xargs is used then find is run and returns all .txt files which are then become a list of inputs for the command cksum.  Where the command is now cksum {file1}.txt {file2}.txt.  It creates a list of arguments from the standard input

>>Example: find *.txt | xargs cksum
  -------



 

