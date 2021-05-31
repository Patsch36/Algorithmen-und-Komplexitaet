#include <fstream>
#include <string>
#include <vector>
#include <iostream>

class sort
{
private:
    std::vector<int> _dvec;
    int _length;

    // Helper functions

    void swap(int *xp, int *yp);
    void merge(int l, int m, int r);
    void mergeSortAlg(int l, int r);
    void heapSortAlg(int n);
    void heapify(int n, int i);
    int partition (int low, int high);
    void quickSortAlg(int low, int high);


public:
    // Necessary functions

    sort(std::string path);
    void printData();
    void uploadData(std::string output_path);

    //Sorting Algorithms

    void selectionSort();
    void bubbleSort();
    void insertionSort();
    void mergeSort();
    void heapSort();

    void quickSort();
};
