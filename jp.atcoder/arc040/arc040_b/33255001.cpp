#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, r;
  string s;
  cin >> n >> r >> s;
  vector<int> a(n * 2);
  for(int i = 0; i < n; i++)
    if(s[i] == 'o') {
      a[i + n]++;
      a[i + n - 1]--;
    }
  int cnt = 0;
  int last = 0;
  for(int i = n * 2 - 1; i >= n; i--) {
    if(a[i] == 0) {
      a[i]++;
      cnt++;
      last = max(last, i - r + 1 - n);
      a[i - r]--;
    }
    a[i - 1] += a[i];
  }
  cout << cnt + last << endl;
}
