this one is a bit hard since we dont have the provision of the binary. when i try to remote to the server, the userhome directory doesnt have the file flaghasher. so we had to use the find command to get it. and we cannot redirect the errors to the /dev/null. but we still found the file location.
![[Pasted image 20251016085051.png]]
so now lets see what it does. i checked the PATH that the system uses to run the binaries and the location of the binary was included so i just ran `flaghasher` and i was abel to see it run. it does the same thing as in the hash-only_1. And when i tried to see its content using the string command, it had the bash command hard coded as well. so may be we can try to hijack the path again. lets see if its expected 
![[Pasted image 20251016085849.png]]
not so quick. path is a read only variable.
lets try a bash function hijack.... hehehe
okay we are logged into a restricted shell `rbash` and this is going to be harder than we thought.  A restricted shell `rbash` is a special limited version of a restricted bash that is meant to limit the what a user can do in there shell. This is made to make sure that the user logged in can only run commands in the $PATH that u control. the following are restricted 
- running cd / (to change directory)
- setting or unsetting the $PATH, $SHELL, $ENV, $BASH_ENV
- using exec to replace the shell process 
- redirecting output (>, >>)
- using `/` to run commands outside `$PATH`
- importing functions from the environment 
- starting another shell like (`/bin/bash`)
-