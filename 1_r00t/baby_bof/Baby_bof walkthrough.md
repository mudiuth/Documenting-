i downloaded the file to my machine using the wget command then started my enumeration. the file is a binary but it doesnt have some security parameters according to the output of the check sec command as shown below. 
![[Pasted image 20251015000519.png]]
the file didnt have the canary, it was not having the PIE enabled and it had the NX enabled so we cannot send s shellcode. and neither was it stripped. 
when i run the binary, it generates the response below 
![[Pasted image 20251015083412.png]]
it gives you the address to the win -function, gives u some time to input a payload and then closes with bye! . this told me that in one way or the other, i had to overwrite the return address so it is the address to the win function. but then we dont know what space we have between these two. 