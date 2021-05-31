#include<time.h>

#include "sort.h"

int main( int argc, char **argv )
{
    sort* sorter = new sort(argv[2]);
    clock_t start, stop;

    std::string raw_op = argv[1];
    std::string op = raw_op.substr (1);
    if(op == "selection"){
        start = clock();
        sorter->selectionSort();
        stop = clock();
    }else if(op == "bubble"){
        start = clock();
        sorter->bubbleSort();
        stop = clock();
    } else if(op == "insertion"){
        start = clock();
        sorter->insertionSort();
        stop = clock();
    } else if (op == "merge"){
        start = clock();
        sorter->mergeSort();
        stop = clock();
    } else if (op == "heap"){
        start = clock();
        sorter->heapSort();
        stop = clock();
    } else if (op == "quick"){
        start = clock();
        sorter->quickSort();
        stop = clock();
    }else{
        std::cerr << "No valid operation" << std::endl;
    }

    std::cout << "used time: " << (float) (stop - start) / CLOCKS_PER_SEC << " seconds" << std::endl;

    //sorter->printData();
    sorter->uploadData(argv[3]);

    system("pause");
    return 0;
}