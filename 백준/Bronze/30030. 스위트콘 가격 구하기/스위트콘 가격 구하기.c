#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void)
{
	int original_price;
	int total_price_with_tax;

	scanf("%d", &total_price_with_tax);

	original_price = total_price_with_tax * 10 / 11;

	printf("%d", original_price);

	return 0;
}
