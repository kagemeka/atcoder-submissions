#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<long long> lucas(87);
  lucas[0] = 2; lucas[1] = 1;
  for (int i = 2; i < 87; i++) {
    lucas[i] = lucas[i-1] + lucas[i-2];
  }
  int n;
  cin >> n;
  cout << lucas[n] << '\n';
  return 0;
}
