#include <iostream>
#include <vector>
#include <limits>
using namespace std;


template<typename T>
std::vector<T> longest_increasing_sequence(const std::vector<T>& a) {
  T inf = std::numeric_limits<T>::max();
  std::vector<T> lis(a.size(), inf);
  for (const T& x: a) *std::lower_bound(lis.begin(), lis.end(), x) = x;
  auto i = std::lower_bound(lis.begin(), lis.end(), inf);
  return std::vector<T>(lis.begin(), i);
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> c[i];
  auto lis = longest_increasing_sequence(c);
  cout << n - lis.size() << '\n';
}
