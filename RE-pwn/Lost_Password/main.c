#include <stdio.h>
#include <string.h>
char man[] = "CTF{HaC";

int main(int argc, char *argv[])
{
	int arr[] = {158, 134, 165, 178, 160, 180, 161, 208};
	if (argc == 2)
	{
		printf("Checking %s\n", argv[1]);
		if (strcmp(argv[1], "mingw.exe") == 0)
		{
			for (int i = 0; i < 8; i++)
			{
				printf("%c", arr[i] - 83);
			}
		}
		else
		{
			printf("WRONG!\n");
		}
	}
	else
	{
		printf("What you doin?? Need Argument\n");
	}
}
