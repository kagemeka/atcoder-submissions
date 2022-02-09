#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}
long long lcm(long long a, long long b) {return abs(a / gcd(a, b) * b);}

long long a, b, c, d;

long long count(long long n) {
  return n - (n / c + n / d - n / lcm(c, d));
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  cin >> a >> b >> c >> d;
  long long ans = count(b) - count(a-1);
  cout << ans << '\n';
  return 0;

}
