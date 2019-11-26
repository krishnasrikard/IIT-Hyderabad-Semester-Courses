#define _GNU_SOURCE
#include <unistd.h> //wrapper for syscalls
#include <sys/syscall.h> // loc: /usr/src/include/i386-linux-gnu/bits/syscall.h, defines syscall numbers/Macros
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

void main()
{
	printf("Calling Status.c");
	execve("a.out",NULL,1);

}