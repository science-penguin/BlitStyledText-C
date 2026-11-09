#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
        int index0 = 3;
        if(argc < 3) {
                printf("it did not provide a width and height");
                return 1;
        }
        int height = atoi(argv[1]);
        int width = atoi(argv[2]);
        if(argc != height * width * 2 + 3) {
                printf("you did not provide enough arguments for the width and height provided");
                return 1;
        }
        printf("\e[1;1H\e[2J");
        for(int index1 = 0; index1 < height; index1++) {
                for(int index2 = 0; index2 < width; index2++) {
                        printf("\033[1;%sm%s\033[1;0m", argv[index0], argv[index0 + 1]);
                        index0 += 2;
                }
                printf("\n");
        }
        return 0;
}
