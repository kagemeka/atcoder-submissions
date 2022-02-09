#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int k;
  cin >> k;
  vector<int> cnt(k + 1);
  for (int i = 1; i < k + 1; i++) {
    for (int j = 1; j < k + 1; j++) {
      cnt[gcd(i, j)]++;
    }
  }
  int res = 0;
  for (int i = 1; i < k + 1; i++) {
    for (int j = 1; j < k + 1; j++) {
      res += cnt[i] * gcd(i, j);
    }
  }
  cout << res << '\n';
  return 0;
}
