#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}
long long lcm(long long a, long long b) {return abs(a / gcd(a, b) * b);}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int k;
  cin >> k;
  long long res = 0;
  for (int i = 1; i < k + 1; i++) {
    for (int j = 1; j < k + 1; j++) {
      int g = gcd(i, j);
      for (int l = 1; l < k + 1; l++) {
        res += gcd(g, l);
      }
    }
  }
  cout << res << '\n';
  return 0;
}
