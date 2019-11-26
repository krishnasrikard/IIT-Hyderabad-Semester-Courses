#include <stdio.h>
#include <sys/types.h> /* Primitive System Data Types */
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{

fprintf(stdout,"Parent PID:%d\n",getpid());
fflush(stdout);

while(fork())
	wait(NULL);

fprintf(stdout,"My PID:%d and My Parent PID:%d\n",getpid(),getppid());

return 0;

}