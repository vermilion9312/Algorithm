#include <stdio.h>

int main(void)
{
	int empty_container[6];
	int total_amount = 0;

	for (int i = 0; i < 6; i++)
	{
		scanf("%d", &empty_container[i]);
		total_amount += 5 * empty_container[i];
	}

	printf("%d", total_amount);

	return 0;
}