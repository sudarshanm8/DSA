#include <iostream>
using namespace std;
int main()
{
    int n;
    std::cin>>n;
    while (n > 0)
        {
            int digit = n%10;
            n /= 10;
            cout<<digit<<" ";
        }

    return 0;
}
