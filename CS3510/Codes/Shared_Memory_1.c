#include <fcntl.h>
#include <string.h>
#include <sys/shm.h>
#include <sys/stat.h>

#define MAX_LEN 10000

struct region
{
/* Defines "structure" of shared memory */
int len;
char buf[MAX_LEN];
};

struct region *rptr;
int fd;
char * msg=“Hello”;

/* Create shared memory object and set its size */

fd = shm_open("/myregion", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);

if (fd == -1)
{
	/* Handle error */;
	printf("Error in Opening\n");
} 

if (ftruncate(fd, sizeof(struct region)) == -1)
{

}

... /* Handle error */;
/* Map shared memory object to process’ address space */

rptr = mmap(NULL, sizeof(struct region), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

if (rptr == MAP_FAILED)

/* Handle error */;
/* Now we can refer to mapped region using fields of rptr */
sprintf(rptr,"%s",msg); //write to shared memory

rptr+=strlen(msg);