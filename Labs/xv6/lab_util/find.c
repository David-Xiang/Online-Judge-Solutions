#include "kernel/fcntl.h"
#include "kernel/fs.h"
#include "kernel/stat.h"
#include "user/user.h"

void
find(char *dir, char *file)
{
  int fd;
  struct dirent de;
  struct stat st;
  char buf[512], *p;

  if((fd = open(dir, O_RDONLY)) < 0) {
    fprintf(2, "find: cannot open %s\n", dir);
    return;
  }
  if(fstat(fd, &st) < 0) {
    fprintf(2, "find: cannot stat %s\n", dir);
    close(fd);
    return;
  }
  if(st.type != T_DIR) {
    close(fd);
    return;
  }

  // printf("list dir %s\n", dir);
  while(read(fd, &de, sizeof(de)) == sizeof(de)) {
    if(de.inum == 0)
      continue;
    if(strcmp(de.name, ".") == 0) {
      continue;
    }
    if(strcmp(de.name, "..") == 0) {
      continue;
    }
    if(strcmp(de.name, file) == 0) {
      // found file
      printf("%s/%s\n", dir, file);
    }

    strcpy(buf, dir);
    p = buf + strlen(dir);
    strcpy(p, "/");
    p++;
    strcpy(p, de.name);

    find(buf, file);
  }
  close(fd);
}

int
main(int argc, char *argv[])
{
  if(argc != 3) {
    fprintf(2, "Usage: find dir file");
    exit(1);
  }

  find(argv[1], argv[2]);
  exit(0);
}
