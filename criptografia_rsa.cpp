#include <iostream>
#include <string>
#include <cmath>
using namespace std;

void decrypt(string msg, int priv_k, int dcrp)
{
    int i = 0, t = 0;
    int *v = new int[t];
    while (i <= msg.length())
    {
    }
};

long long module(long long num, long long exp, long long mod)
{
    long long res = 1;
    while (exp > 0)
    {
        if (exp & 1)
        {
            res = (res * num) % mod;
        }
        num = (num * num) % mod;
        exp >>= 1;
    }
    return res;
}

int main()
{
    // n = 67 x 71, tot = (67 - 1) x (71 - 1) = 4620; 3079E = 1 + k4620
    long long x, n = 4757, D = 3079;
    string message = "3671-435-3527-2180-1016-510-807-4684-4188-4449-2194-4329-345-1174-1016-2264-1447-4395-1611-3671-345-237";
    while (true)
    {
        cin >> x;
        if (x == 0)
        {
            break;
        }
        else
        {
            cout << module(x, D, n) << " ";
        }
    }
}