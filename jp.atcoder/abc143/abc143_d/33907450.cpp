#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    for(int j = i + 1, k = j + 1; j < n; j++) {
      while(k < n && a[k] < a[i] + a[j]) k++;
      cnt += (k - j - 1);
    }
  }
  cout << cnt << endl;
}
