format string is a kind of vulnerability where the format string function interprets the entered input as the command. this happens when the format string has no specifiers.. when the user inputs data, the format function will treat the data as the commands. 

**writing to memory using format strings in a format string vulnerability** 
in some exploits, we need to write and call an address that is on the memory of the stack.. this is kind of complex than writing just the address to the memory 
https://www.scitepress.org/publishedPapers/2024/128524/pdf/index.html
**%p prints the value that is on the stack as the memory** it doesnt care what the address it found on the stack holds. it just prints the value t finds in the stack batch at that given time when it is used. during an execution of a program, the stack pointer holds addresses to the data that the cpu needs or is required to access. for example when the binary is executed, and may be the program requires the cpu to access a variable X on address 0xfffff, the stack pointer will hold the address 0xfffff. so when the format function purses `%p`, the output will be for 0xffff

**%s reads the value from the stack pointer, treats it as memory, navigates to that memory address and reads everything there until it reaches NULL or /n**. now this will read 0xffff (using the above example) goes to the memory address and prints the bytes it finds in the address untill it finds a NULL, or /n or next line  this is called `pass by reference `
![[Pasted image 20251023142127.png]]
this is how a stack looks like in the alignment.

printf(“\xef\xbe\xad\xde%x%x%x%s”, A, B, C);
suppose this is my pay load, this tells the cpu to skip to the 3rd position of the stack (using %x) and then treat the fst 5 bytes (the address in little endian) as an address and read what that address has and gives it to me as a byte... right?