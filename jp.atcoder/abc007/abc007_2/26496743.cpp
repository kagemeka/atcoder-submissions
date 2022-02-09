#include <iostream>
#include <string>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  cout << (s == "a" ? "-1" : "a") << '\n';
}
