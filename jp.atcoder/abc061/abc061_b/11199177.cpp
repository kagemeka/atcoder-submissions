#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> res(n);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    res[a-1]++;
    res[b-1]++;
  }

  for (int i = 0; i < n; i++) {
    cout << res[i] << endl;
  }
  return 0;
}
