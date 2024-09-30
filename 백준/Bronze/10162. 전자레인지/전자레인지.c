#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void)
{
	int cooking_time;
	int button[3] = { 300, 60, 10 };
	int quetient[3] = { 0, };

	scanf("%d", &cooking_time);


	for (int i = 0; i < 3; i++)
	{
		quetient[i] = cooking_time / button[i];
		cooking_time %= button[i];
	}

	if (cooking_time)
	{
		printf("%d", -1);
	}
	else
	{
		for (int i = 0; i < 3; i++)
		{
			printf("%d ", quetient[i]);
		}
	}

	return 0;
}
