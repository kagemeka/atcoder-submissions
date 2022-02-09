#include <iostream>
#include <vector>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n = 6;
  vector<int> a(n);
  for (int i = 0; i < n; i++) a[i] = i + 1;
  int k; cin >> k;
  k %= n * (n - 1);
  for (int i = 0; i < k; i++) {
    swap(a[i % (n - 1)], a[i % (n - 1) + 1]);
  }
  for (int i = 0; i < n; i++) cout << a[i];
  cout << '\n';
}
