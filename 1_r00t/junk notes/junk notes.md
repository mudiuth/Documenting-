ELF (executable and linkable format) is an executable file format in the unix like operating systems including linux. this is like the .exe file in windows... (executable). u can as well see if the stack they used  is legit. 

**chroot**
The chroot command is a command used to switch the root file system to another directory and it is used in the way `sudo chroot /newroot` this will change the current root directory called a chroot jail. all other sudoers will be limited to access files that in this rooted file system. otherwise, there wont be access to files outside this directory even to the root user. However the real system still exists and can be recovered. 

