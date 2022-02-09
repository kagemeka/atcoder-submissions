#include <bits/stdc++.h>
using namespace std;

unordered_set<long long> divisors(long long n) {
  unordered_set<long long> res;
  for (int i = 1; i < floor(sqrt(n)) + 1; i++) {
    if (n % i == 0) {res.insert(i); res.insert(n / i);}
  }
  res.erase(1);
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long n;
  cin >> n;
  long long cnt = divisors(n - 1).size();
  for (long long const &i : divisors(n)) {
    long long m = n;
    while (m % i == 0) m /= i;
    cnt += (m - 1) % i == 0;
  }
  cout << cnt << '\n';
  return 0;
}
