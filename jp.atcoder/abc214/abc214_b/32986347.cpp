#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int s, t;
  cin >> s >> t;

  int k = 101;

  int cnt = 0;
  for (int i = 0; i < k * k * k; i++) {
    int j = i;
    int a = j % k;
    j /= k;
    int b = j % k;
    int c = j / k;
    cnt += a + b + c <= s && a * b * c <= t;
  }
  cout << cnt << endl;
}
