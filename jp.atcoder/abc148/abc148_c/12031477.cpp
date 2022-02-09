#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}
long long lcm(long long a, long long b) {return abs(a / gcd(a, b) * b);}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int a, b; cin >> a >> b;
  cout << lcm(a, b) << '\n';
  return 0;
}
