#include <time.h> 
#include <stdio.h>

clock_t start, stop;

int main()
{
    start = clock();     
 
    // Hier laeuft die Zeit ...
      
    stop = clock();

    printf("Laufzeit: %.3f Sekunden\n", (float) (stop - start) / CLOCKS_PER_SEC);     
    
    return 0;  
}
      