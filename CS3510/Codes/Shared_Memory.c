#include <stdio.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <stdio.h>
#include <sys/types.h> /* Primitive System Data Types */
#include <unistd.h>
#include <sys/wait.h>

// Example using System V shared memory objects
// shm_open and mmap in POSIX

void main(int argc, char **argv)
{

char* shared_memory;
const int size = 4096;

int segment_id = shmget(IPC_PRIVATE, size, IPC_CREAT | 0666);

int cpid = fork();

if (cpid == 0)
{
	shared_memory = (char*) shmat(segment_id, NULL, 0);//attach
	sprintf(shared_memory, "Hi from process %d",getpid());
}

else
{
	wait(NULL);
	shared_memory = (char*) shmat(segment_id, NULL, 0);//attach
	printf("Process %d read: %s\n", getpid(), shared_memory);
	shmdt(shared_memory);//detach
	shmctl(segment_id, IPC_RMID, NULL);//remove segment
}

}