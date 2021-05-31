#include <fstream>
#include <string>
#include <vector>
#include <iostream>

class sort
{
private:
    std::vector<int> _dvec;
    int _length;
    void swap(int *xp, int *yp);

public:
    sort(std::string path);
    void printData();
    void uploadData(std::string output_path);

    void selectionSort();
    void bubbleSort();
    void insertionSort();

};
