#include <stdio.h>

#define STRINGIZE(x) #x
#define STRINGIZE_VALUE_OF(x) STRINGIZE(x)


int main()
{
    printf("%s", STRINGIZE(name));
}