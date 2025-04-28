#include "kernel/types.h"
#include "user/user.h"

void
primes(int, int) __attribute__((noreturn));

void
primes(int n, int read_fd)
{
  printf("prime %d\n", n);
  int create_child = 0;
  int num;
  int recv = read(read_fd, (void *)&num, 4);
  int p[2];
  while(recv != 0) {
    if(num % n != 0) {
      if(!create_child) {
        pipe(p);
        if(fork() == 0) {
          close(read_fd);
          close(p[1]);
          primes(num, p[0]);
        }
        close(p[0]);
        create_child = 1;
      } else {
        write(p[1], &num, 4);
      }
    }
    recv = read(read_fd, (void *)&num, 4);
  }
  if(create_child) {
    close(p[1]);
    wait(0);
  }
  close(read_fd);
  exit(0);
}

int
main(int argc, char *argv[])
{
  int p[2];
  pipe(p);
  if(fork() == 0) {
    close(p[1]);
    primes(2, p[0]);
  }
  close(p[0]);
  for(int i = 3; i <= 280; ++i) {
    write(p[1], (void *)&i, 4);
  }
  close(p[1]);
  wait(0);
  exit(0);
}
