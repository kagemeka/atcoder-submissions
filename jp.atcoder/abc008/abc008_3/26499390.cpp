#include <iostream>
#include <vector>
#include <map>
#include <iomanip>
using namespace std;


// template <typename T>
// // std::vector<int>

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> c[i];

  map<long long, int> divcnt;
  for (const long long &x : c) {
    for (const long long &y : c) {
      divcnt[x] += x % y == 0;
    }
  }

  double ex = .0;
  for (const long long &x : c) {
    ex += (double)((divcnt[x] + 1) / 2) / divcnt[x];
  }
  cout << setprecision(8) << ex << '\n';

}
