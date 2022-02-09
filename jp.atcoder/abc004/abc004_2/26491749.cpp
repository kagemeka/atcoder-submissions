#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  vector<string> c(4);
  for (int i = 0; i < 4; i++) getline(cin, c[i]);
  for (int i = 3; i > -1; i--) {
    auto row = c[i];
    reverse(row.begin(), row.end());
    cout << row << '\n';
  }
}
