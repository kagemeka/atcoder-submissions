#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long n;
  cin >> n;
  long long x = n;
  int rank = 0;
  while (x > 1) {
    x /= 2;
    rank++;
  }
  bool flag = rank & 1;
  int cnt = 0;
  while (x <= n) {
    x = ((cnt & 1) ^ flag) ? 2 * x : 2 * x + 1;
    cnt++;
  }
  string ans = (cnt & 1) ? "Aoki" : "Takahashi";
  cout << ans << '\n';
  return 0;
}
