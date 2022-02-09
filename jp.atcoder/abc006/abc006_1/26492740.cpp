#include <iostream>
#include <string>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  cout << ((n % 3 == 0) ? "YES" : "NO") << '\n';
}
