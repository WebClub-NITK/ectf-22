# Lost Password

Author: Asim Jawahir

Flag: `CTF{HaCK3R_MaN}`

## Problem Statement

Bob lost his super-secret password to access his coolcoin wallet. Bob knows the password is somewhere in the main file! Help bob retrieve the password so he can spend his coolcoin!

## Relevant files / links

- [main](./main)

## Hint

Two strings, one can't be directly accessed while the other can(kind of).

## Solution

### The program has two parts. 

1. 
    Use the following command.

    ```sh
    strings main
    ```

    You would get a bunch of strings present in the file. By going through the text, you would come across `CTF{HaC`, which is the first part of the flag.

2. 
    Use the following command.
    
    We are using GNU Debugger (gdb) to see what is going on inside the program.
    ```sh
    gdb
    ```
    We use the following command to read symbols from main.
    ```sh
    file main
    ```
    Set the disassembly flavor to intel. so that the disassembly looks more readable
    ```sh
    set disassembly-flavor intel
    ```
    Then the following command is used to view the assembly code of main.
    ```sh
    disassemble main
    ```
    The assembly code of main is the following
    ```asm
    0x00000000000011c9 <+0>:    endbr64 
    0x00000000000011cd <+4>:    push   rbp
    0x00000000000011ce <+5>:    mov    rbp,rsp
    0x00000000000011d1 <+8>:    sub    rsp,0x50
    0x00000000000011d5 <+12>:   mov    DWORD PTR [rbp-0x44],edi
    0x00000000000011d8 <+15>:   mov    QWORD PTR [rbp-0x50],rsi
    0x00000000000011dc <+19>:   mov    rax,QWORD PTR fs:0x28
    0x00000000000011e5 <+28>:   mov    QWORD PTR [rbp-0x8],rax
    0x00000000000011e9 <+32>:   xor    eax,eax
    0x00000000000011eb <+34>:   mov    DWORD PTR [rbp-0x30],0x9e
    0x00000000000011f2 <+41>:   mov    DWORD PTR [rbp-0x2c],0x86
    0x00000000000011f9 <+48>:   mov    DWORD PTR [rbp-0x28],0xa5
    0x0000000000001200 <+55>:   mov    DWORD PTR [rbp-0x24],0xb2
    0x0000000000001207 <+62>:   mov    DWORD PTR [rbp-0x20],0xa0
    0x000000000000120e <+69>:   mov    DWORD PTR [rbp-0x1c],0xb4
    0x0000000000001215 <+76>:   mov    DWORD PTR [rbp-0x18],0xa1
    0x000000000000121c <+83>:   mov    DWORD PTR [rbp-0x14],0xd0
    0x0000000000001223 <+90>:   cmp    DWORD PTR [rbp-0x44],0x2
    0x0000000000001227 <+94>:   jne    0x129c <main+211>
    0x0000000000001229 <+96>:   mov    rax,QWORD PTR [rbp-0x50]
    0x000000000000122d <+100>:  add    rax,0x8
    0x0000000000001231 <+104>:  mov    rax,QWORD PTR [rax]
    0x0000000000001234 <+107>:  mov    rsi,rax
    0x0000000000001237 <+110>:  lea    rdi,[rip+0xdc6]        # 0x2004
    0x000000000000123e <+117>:  mov    eax,0x0
    0x0000000000001243 <+122>:  call   0x10c0 <printf@plt>
    0x0000000000001248 <+127>:  mov    rax,QWORD PTR [rbp-0x50]
    0x000000000000124c <+131>:  add    rax,0x8
    0x0000000000001250 <+135>:  mov    rax,QWORD PTR [rax]
    0x0000000000001253 <+138>:  lea    rsi,[rip+0xdb7]        # 0x2011
    0x000000000000125a <+145>:  mov    rdi,rax
    0x000000000000125d <+148>:  call   0x10d0 <strcmp@plt>
    0x0000000000001262 <+153>:  test   eax,eax
    0x0000000000001264 <+155>:  jne    0x128e <main+197>
    0x0000000000001266 <+157>:  mov    DWORD PTR [rbp-0x34],0x0
    0x000000000000126d <+164>:  jmp    0x1286 <main+189>
    0x000000000000126f <+166>:  mov    eax,DWORD PTR [rbp-0x34]
    0x0000000000001272 <+169>:  cdqe   
    0x0000000000001274 <+171>:  mov    eax,DWORD PTR [rbp+rax*4-0x30]
    0x0000000000001278 <+175>:  sub    eax,0x53
    0x000000000000127b <+178>:  mov    edi,eax
    0x000000000000127d <+180>:  call   0x1090 <putchar@plt>
    0x0000000000001282 <+185>:  add    DWORD PTR [rbp-0x34],0x1
    0x0000000000001286 <+189>:  cmp    DWORD PTR [rbp-0x34],0x7
    0x000000000000128a <+193>:  jle    0x126f <main+166>
    0x000000000000128c <+195>:  jmp    0x12a8 <main+223>
    0x000000000000128e <+197>:  lea    rdi,[rip+0xd86]        # 0x201b
    0x0000000000001295 <+204>:  call   0x10a0 <puts@plt>
    0x000000000000129a <+209>:  jmp    0x12a8 <main+223>
    0x000000000000129c <+211>:  lea    rdi,[rip+0xd7f]        # 0x2022
    0x00000000000012a3 <+218>:  call   0x10a0 <puts@plt>
    0x00000000000012a8 <+223>:  mov    eax,0x0
    0x00000000000012ad <+228>:  mov    rdx,QWORD PTR [rbp-0x8]
    0x00000000000012b1 <+232>:  xor    rdx,QWORD PTR fs:0x28
    0x00000000000012ba <+241>:  je     0x12c1 <main+248>
    0x00000000000012bc <+243>:  call   0x10b0 <__stack_chk_fail@plt>
    0x00000000000012c1 <+248>:  leave  
    0x00000000000012c2 <+249>:  ret   
    ```

    We first set a breakpoint at the start of main, and then start the debugging session.
    ```sh
    break *main
    start
    continue
    ```
    We notice that the program prints out the string "What you doin?? Need Argument" so we now run the program with any argument
    ```sh
    start (any input)
    ```
    after we start the debugging session, we keep running the command `ni` to go through the code until we come across the message at address `0x0000555555555248.`
    ```sh
    Checking (input entered)
    ```
    At `0x000000000000125d` we see there's a call to strcmp function(when two strings are same strcmp returns 0). Here it's comparing the input supplied by us to some string. So we break at jne instruction and modify eax register(which is  used to store the return value of functions). The address of that instruction is `0x0000555555555262`, so we set a breakpoint there and set eax to 0.
    ```sh
    break *0x0000555555555262
    start
    continue
    set $eax=0
    ```
    we now use continue to print the rest of the program
    ```sh
    continue
    ```

    And you would get the following message `K3R_MaN}`

Combining both part 1 and part 2, we get: `CTF{HaCK3R_MaN}`

