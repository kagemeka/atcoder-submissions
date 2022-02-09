#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string n;
  cin >> n;
  int tot = 0;
  for (char &d : n) tot += d - '0';
  string ans = (stoi(n) % tot) ? "No" : "Yes";
  cout << ans << '\n';
  return 0;
}
