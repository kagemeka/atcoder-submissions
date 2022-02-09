#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string keyboard = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW";
  vector<string> res = {"Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"};
  string s;
  cin >> s;
  cout << res[keyboard.find(s)] << '\n';
  return 0;
}
