#define _GNU_SOURCE
#include <unistd.h> //wrapper for syscalls
#include <sys/syscall.h> // loc: /usr/src/include/i386-linux-gnu/bits/syscall.h, defines syscall numbers/Macros
#include <sys/types.h>
#include <stdio.h>

int main()
{
	while(1)
	{
		type_prompt();
		read_command(command,parameters);

		if(fork() != 0)
		{
			waitpid(-1,&status,0);
		}

		else
		{
			execve(command,parameters,0);
		}
	}
}