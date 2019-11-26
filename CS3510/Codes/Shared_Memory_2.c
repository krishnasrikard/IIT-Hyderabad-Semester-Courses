#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <stdio.h>
#include <sys/types.h> /* Primitive System Data Types */
#include <unistd.h>
#include <sys/wait.h>

int main()
{
	/* name of the shared memory object */
	const char *name = "/myregion";
	/* shared memory file descriptor */
	
	int shmfd;
	/* pointer to shared memory obect */

	void *ptr;
	/* open the shared memory object */
	shmfd = shm open(name, O_RDONLY, 0666);
	/* memory map shared memory object to process’ address space */
	ptr = mmap(0, sizeof(struct region), PROT_READ, MAP_SHARED,shmfd, 0);
	/* read from the shared memory object */
	printf("%s",(char *)ptr);
	/* remove the shared memory object */
	shm_unlink(name);
	return 0;

}
