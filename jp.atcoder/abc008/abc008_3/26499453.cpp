#include <iostream>
#include <vector>
#include <map>
#include <iomanip>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> c[i];

  vector<int> divcnt(n);
  for (int i = 0; i < n; i++) {
    for (const int &y : c) {
      divcnt[i] += c[i] % y == 0;
    }
  }

  double ex = .0;
  for (const int &x : divcnt) {
    ex += (double)((x + 1) / 2) / x;
  }
  cout << setprecision(8) << ex << '\n';

}
