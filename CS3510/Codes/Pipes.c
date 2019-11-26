#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <stdio.h>
#include <sys/types.h> /* Primitive System Data Types */
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(void)
{
int pid;
char buffer[1024];
int fd[2];
pipe(fd); /* ordinary pipes; fd[0] is for read-end, fd[1] is for write-end of pipe */
pid = fork();

if (pid == 0) /* child */
{
	int count;
	close(fd[0]); /* close unused READ end, child will write */
	/* prompt user for input */
	printf("Input: ");
	fgets(buffer, sizeof(buffer), stdin);
	printf("Child: Message is %s", buffer);
	/* write to the pipe (include NUL terminator) */
	count = write(fd[1], buffer, strlen(buffer) + 1); //pipe is a special type of file
	printf("Child: Wrote %i Bytes\n", count);
	close(fd[1]);
	exit(0);
}

else /* parent */
{
	int count;
	close(fd[1]); /* close unused WRITE end */
	wait(NULL); /* reap the child */
	/* read from the pipe */
	count = read(fd[0], buffer, sizeof(buffer));
	printf("Parent: Message is %s", buffer);
	printf("Parent: Read %i Bytes\n", count);
	close(fd[0]);
}

}