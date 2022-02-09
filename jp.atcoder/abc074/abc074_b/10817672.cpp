#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k;
  cin >> n >> k;

  int tot = 0;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;

    tot += min(x, k - x) * 2;
  }
  cout << tot << endl;

}
