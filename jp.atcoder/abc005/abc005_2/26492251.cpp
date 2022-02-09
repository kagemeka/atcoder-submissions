#include <iostream>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n; cin >> n;
  int mn = 100;
  for (int i = 0; i < n; i++) {
    int t; cin >> t;
    if (t < mn) mn = t;
  }
  cout << mn << '\n';
}
