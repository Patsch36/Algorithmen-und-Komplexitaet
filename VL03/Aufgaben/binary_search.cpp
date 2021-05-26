#include <string>
#include <iostream>
#include <chrono>


// recursive programmed binary search
int binarySearchRek(int arr[], int l, int r, int x)
{
	if (r >= l)
	{
		int m = (l + r) / 2;

		if(arr[m] == x)
			return m;

		if (arr[m] > x)
			return binarySearchRek(arr, l, m - 1, x);

		return binarySearchRek(arr, m + 1, r, x);
	}
	return -1;
}

// iterative programmed binary search
int binarySearchIt(int arr[], int l, int r, int x)
{
	while (r >= l)
	{
		int m = (l + r) / 2;
		if(arr[m] == x)
			return m;

		if(x < arr[m])
			r = m - 1;

		else
			l = m + 1;
	}
	return -1;
}


int main()
{

	// ===== Set up memory and data ==========================================================
	const int arrlen = 2000000000;
	std::chrono::time_point<std::chrono::steady_clock>start, end;
	
	int* arr = new int[arrlen];

	for(int i = 1; i <= arrlen; i++)
	{
		arr[i-1] = i;
	}

	int x = 1235;


	// ===== Calculation iterative ===========================================================
	std::cout << "Rekursiv, " << arrlen << " Elemente, gesucht ist Element " << x << std::endl;
	start = std::chrono::steady_clock::now();

	std::cout << "Position: " << binarySearchRek(arr, 0, arrlen - 1, x) << std::endl;

	end = std::chrono::steady_clock::now();
	std::chrono::duration<double> elapsed = end - start;
	auto int_us = std::chrono::duration_cast<std::chrono::microseconds>(elapsed);

	std::cout << int_us.count() << " us" << std::endl << std::endl;


	// ===== Calculation recursiv ============================================================
	std::cout << "Iterativ, " << arrlen << " Elemente, gesucht ist Element " << x << std::endl;
	start = std::chrono::steady_clock::now();

	std::cout << "Position: " << binarySearchIt(arr, 0, arrlen - 1, x) << std::endl;

	end = std::chrono::steady_clock::now();
	elapsed = end - start;
	auto int_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(elapsed);

	std::cout << int_ns.count() << " ns ~ " << (float) int_ns.count() / 1000 << " us" << std::endl;


	// ===== Clean up Memory =================================================================
	delete(arr);

	system("pause");
	return 0;
}
