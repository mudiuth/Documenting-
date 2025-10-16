this is a pico ctf challenge.
when i tried to make some checking with checksec, below is what i found out 
![[Pasted image 20251016010704.png]]
so i did ssh into the server and tried to run the binary.  all it could do is to out put the md5 hash of the flag. good enough it could shpw the source of the flag. 
![[Pasted image 20251016010952.png]]
we dont have writing rights to the binary and the binary has the suid bit set.
![[Pasted image 20251016011035.png]]
we as well dont have any function that seems to be inputing anything... 
according to the look of things,  the target is to make sure that instead of getting the md5 hash, we need the flag to be printed. checking the binary using ghidra, the command was hard coded in the binary 
![[Pasted image 20251016011308.png]]
so we need to make this become cat root/flag.txt. we try path hijacking. 
fst we go to the /tmp directory and make a directory called exploit. we then get out cat command into md5sum file change the path and then goo back and run the binary and below is how it looks like 
![[Pasted image 20251016012431.png]]
![[Pasted image 20251016012457.png]]
and there is the flag. 

