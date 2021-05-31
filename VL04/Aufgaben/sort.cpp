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

void sort::merge(int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
 
    // Create temp arrays
    int L[n1], R[n2];
 
    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = _dvec[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = _dvec[m + 1 + j];
 
    // Merge the temp arrays back into arr[l..r]
 
    // Initial index of first subarray
    int i = 0;
 
    // Initial index of second subarray
    int j = 0;
 
    // Initial index of merged subarray
    int k = l;
 
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            _dvec[k] = L[i];
            i++;
        }
        else {
            _dvec[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of
    // L[], if there are any
    while (i < n1) {
        _dvec[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of
    // R[], if there are any
    while (j < n2) {
        _dvec[k] = R[j];
        j++;
        k++;
    }
}

void sort::mergeSortAlg(int l, int r)
{
    if(l>=r){
            return;//returns recursively
        }
        int m =l+ (r-l)/2;
        mergeSortAlg(l,m);
        mergeSortAlg(m+1,r);
        merge(l,m,r);
}

void sort::mergeSort()
{
    mergeSortAlg(0, _length);
}

void sort::heapSort()
{
    heapSortAlg(_length/2);
}

void sort::heapSortAlg(int n)
{
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(n, i);
 
    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        swap(&_dvec[0], &_dvec[i]);
 
        // call max heapify on the reduced heap
        heapify(i, 0);
}
}

void sort::heapify(int n, int i)
{
    int largest = i; // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2
 
    // If left child is larger than root
    if (l < n && _dvec[l] > _dvec[largest])
        largest = l;
 
    // If right child is larger than largest so far
    if (r < n && _dvec[r] > _dvec[largest])
        largest = r;
 
    // If largest is not root
    if (largest != i) {
        swap(&_dvec[i], &_dvec[largest]);
 
        // Recursively heapify the affected sub-tree
        heapify(n, largest);
    }
}

void sort::quickSort()
{
    quickSortAlg(0, _length - 1);
}

int sort::partition(int low, int high)
{
    int pivot = _dvec[high]; // pivot
    int i = (low - 1); // Index of smaller element and indicates the right position of pivot found so far
 
    for (int j = low; j <= high - 1; j++)
    {
        // If current element is smaller than the pivot
        if (_dvec[j] < pivot)
        {
            i++; // increment index of smaller element
            swap(&_dvec[i], &_dvec[j]);
        }
    }
    swap(&_dvec[i + 1], &_dvec[high]);
    return (i + 1);
}

void sort::quickSortAlg(int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
        at right place */
        int pi = partition(low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSortAlg(low, pi - 1);
        quickSortAlg(pi + 1, high);
    }
}
