#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  double tot = 0;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    double x;
    string u;
    cin >> x >> u;
    tot += (u == "JPY") ? x : x * 380000.0;
  }
  cout << setprecision(6) << tot << '\n';
  return 0;
}
