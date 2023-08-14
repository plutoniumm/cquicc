#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

int ITERS = 50;

FILE *fp;

char *generateValues(int ITERS) {
  int x, y, NUM = time(NULL), RND;
  char *result = (char *)malloc(1024 * sizeof(char));
  char temp[50];

  if (result == NULL) {
    fprintf(stderr, "Memory allocation error");
    exit(1);
  }

  result[0] = '\0';  // Initialize an empty string
  printf("Running on Num: %d\n", NUM);

  for (x = 0; x <= ITERS; x++) {
    for (y = 0; y <= ITERS; y++) {
      NUM = ((NUM * 1103245 + 12345) % 65536);
      NUM = (NUM / 100);
      RND = NUM % 2;

      snprintf(temp, sizeof(temp), "%d,%d,%d\n", x, y, RND);
      strcat(result, temp);
    }
  }

  return result;
}

int main() {
  time_t t;
  char *FILE = "./send.txt";

  srand((unsigned)time(&t));

  while (1) {
    fp = fopen(FILE, "w");

    char *values = generateValues(ITERS);
    fprintf(fp, "%s", values);

    fclose(fp);
    sleep(1);
  }

  return 0;
}
