#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  vector<int> cnt(n, -1);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (a[i] % a[j] == 0) cnt[i]++;
    }
  }
  double ex;
  for (int &c : cnt) {
    ex += (double)((c + 2) / 2) / (c + 1);
  }
  cout << setprecision(10) << ex << '\n';
  return 0;
}
