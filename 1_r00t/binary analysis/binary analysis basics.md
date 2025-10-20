the binary is a file that contains executable code that the computer understands directly. this file includes the instruction set and it is dine by compiling an high level language program that is in languages like c, c++, c# etc. the process of compilation undergoes 4 steps. 
- preprocessing
- compilation
- assembly and 
- linking

**Format Strings**
a format function is a function that converts a primitive variable of a programming language into a human readable format eg `printf, fprintf`
a format string is the argument of a format function which contains texts and parameters `printf ("john is %d years old")`
a format string parameter defines the type of conversion of the format function like `%d, %x, %s, %n`
the format string attacks occur when the input of data in the program is interpreted as a command by the system in the program thus causing abnormal behaviour in the course of the program execution. 
the attack could be executed when the application does not properly sanitize the input from the user. in this case if the format string parameter like `%n` is inserted into the posted data, the string is parsed by the format function and the coversion specified in the parameter is executed. however the format function might be expecting more information and if not supplied, the function could read or write the stack.

if the user can find a way of showing the format string, this means the attacker can win control over the behaviour of the format function and can take advantage of it. 

