when u open some binaries, codes start with 
0x55 and the canary ends with 00.. its a null byte to cover for string over flow 
so i have got the canary address and it is in the 19th position %19$p
![[Pasted image 20251022151804.png]]
the base addresss was in the 6th position ![[Pasted image 20251022152045.png]]

i had also got the offset of the print_flag fucntion using the readelf tool and the gdb 
![[Pasted image 20251022152430.png]]