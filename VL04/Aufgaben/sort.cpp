#include "sort.h"

void sort::swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

sort::sort(std::string path)
{
    std::ifstream input(path);
    if(!input) {
		std::cerr << "Datei wurde nicht gefunden." << std::endl;
		// return EXIT_FAILURE;
	}

	int wert;
    _length = 0;

    while(input >> wert)
    {
        _dvec.push_back(wert);
        _length++;
    }
    
}

void sort::printData()
{
    for(auto value:_dvec)
        std::cout << value << std::endl;
}

void sort::selectionSort()
{
    int i, j, min_idx; 
  
    // One by one move boundary of unsorted subarray 
    for (i = 0; i < _length-1; i++) 
    { 
        // Find the minimum element in unsorted array 
        min_idx = i; 
        for (j = i+1; j < _length; j++)
        {
            if (_dvec[j] < _dvec[min_idx]) 
                min_idx = j; 
        } 
  
        // Swap the found minimum element with the first element
        swap(&_dvec[min_idx], &_dvec[i]); 
    } 
}

void sort::bubbleSort()
{
    int i, j;
   bool swapped;
   for (i = 0; i < _length-1; i++)
   {
     swapped = false;
     for (j = 0; j < _length-i-1; j++)
     {
        if (_dvec[j] > _dvec[j+1])
        {
           swap(&_dvec[j], &_dvec[j+1]);
           swapped = true;
        }
     }
 
     // IF no two elements were swapped by inner loop, then break
     if (swapped == false)
        break;
   }
}

void sort::insertionSort()
{
    int i, key, j;
    for (i = 1; i < _length; i++)
    {
        key = _dvec[i];
        j = i - 1;
 
        /* Move elements of arr[0..i-1], that are
        greater than key, to one position ahead
        of their current position */
        while (j >= 0 && _dvec[j] > key)
        {
            _dvec[j + 1] = _dvec[j];
            j = j - 1;
        }
        _dvec[j + 1] = key;
    }
}

void sort::uploadData(std::string output_path)
{
    std::ofstream out(output_path);
    for(auto value:_dvec)
        out << value << std::endl;
    out.close();
}