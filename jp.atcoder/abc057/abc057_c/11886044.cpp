#include <bits/stdc++.h>
using namespace std;

vector<long long> divisors(long long n) {
  vector<long long> res;
  for (int i = 1; i < int(sqrt(n)) + 1; i++) {
    if (n % i == 0) res.push_back(i);
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long n;
  cin >> n;
  auto res = divisors(n);
  int ans = to_string(n /res[res.size() - 1]).size();
  cout << ans << '\n';
  return 0;
}
