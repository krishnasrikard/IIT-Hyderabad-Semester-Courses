#define _GNU_SOURCE
#include <unistd.h> //wrapper for syscalls
#include <sys/syscall.h> // loc: /usr/src/include/i386-linux-gnu/bits/syscall.h, defines syscall numbers/Macros
#include <sys/types.h>
#include <stdio.h>

void main()
{
	while(1)
	{
		char* command = "ls";
		printf("Calling Status.c");

		execve("st",NULL,NULL);
	}
}