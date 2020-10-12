#include <stdio.h>

#define Stringize(x) #x
#define Stringize_me(x) Stringize(x)

int main()
{
    printf("%s", Stringize_me(name));
}