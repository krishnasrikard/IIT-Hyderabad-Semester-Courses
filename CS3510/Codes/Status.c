#include <stdio.h>
#include <sys/types.h> /* Primitive System Data Types */
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
int i, pid, status;
pid = getpid();

fprintf(stdout, "parent pid = %d\n", pid);

pid = fork();
if (pid == 0) /* child process is always 0 */
{

	for (i= 0; i < 10; ++i)
	{
		fprintf(stdout,"In child: Iteration: %d\n",i);
		sleep(0.1);
	}
	fprintf(stdout, "In child: child exiting\n");
}
	
else /* parent process is non-zero (child's pid) */
{
	//sleep(2); //to force child to run first
	fprintf(stdout, "In Parent: child pid = %d\n", pid);
	fflush(stdout);
	fprintf(stdout, "In Parent: waiting for child\n");
	//wait(NULL); //wait for any child to change state
	//wait(&status); //status is stored here
	//waitpid(-1,&status,0); //wait for any child to change state
	waitpid(pid,&status,0); //wait for pid child to change state
	fprintf(stdout, "In Parent: Child exit status:%d\n",WEXITSTATUS(status));

	if(WIFEXITED(status))
		fprintf(stdout, "In Parent: Child exited normally\n");
	else if(WIFSIGNALED(status))
		fprintf(stdout, "In Parent: Child was killed by a signal!!\n");
	else
		fprintf(stdout, "In Parent: Child exited for other reasons\n");

fprintf(stdout, "In Parent: child terminated\n");
fprintf(stdout, "In Parent: parent exiting\n");
}

return 0;
}