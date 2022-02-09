#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  vector<int> t(n);
  for (int i = 0; i < n; i++) {
    cin >> t[i];
  }

  cout << *min_element(t.begin(), t.end()) << endl;
  return 0;
}
