this one is a bit hard since we dont have the provision of the binary. when i try to remote to the server, the userhome directory doesnt have the file flaghasher. so we had to use the find command to get it. and we cannot redirect the errors to the /dev/null. but we still found the file location.
![[Pasted image 20251016085051.png]]
so now lets see what it does. i checked the PATH that the system uses to run the binaries and the location of the binary was included so i just ran `flaghasher` and i was abel to see it run. it does the same thing as in the hash-only_1. And when i tried to see its content using the string command, it had the bash command hard coded as well. so may be we can try to hijack the path again. lets see if its expected 
![[Pasted image 20251016085849.png]]
not so quick. path is a read only variable.
lets try a bash functio