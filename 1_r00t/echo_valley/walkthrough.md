when u open some binaries, codes start with 
0x55 and the canary ends with 00.. its a null byte to cover for string over flow 
so i have got the canary address and it is in the 19th position %19$p
![[Pasted image 20251022151804.png]]
the base addresss was in the 6th position ![[Pasted image 20251022152045.png]]

i had also got the offset of the print_flag fucntion using the readelf tool and the gdb 
![[Pasted image 20251022152430.png]]
now how we shall get to print the address_of the binary = base_address of the binary + the offset of the function. 
the gold we are looking for is the base of the whole binary. this is because the code addresses are randomised by the PIE (position independent executables)
to get the base of the binary, 
0x55f16f26e413

after getting the golden treasure (our address for the print_flag function) then we try to inject it into the code.. using the format string vulnerability. 