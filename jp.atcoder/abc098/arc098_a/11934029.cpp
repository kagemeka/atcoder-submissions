#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  string s;
  cin >> n >> s;
  int tmp = 0;
  for (int i = 0; i < n; i++) {
    tmp += s[i] == 'E';
  }
  vector<int> res;
  char cur = 'E';
  for (int i = 0; i < n; i++) {
    if (cur == 'W') tmp++;
    if (s[i] == 'E') tmp--;
    res.push_back(tmp);
    cur = s[i];
  }
  cout << *min_element(res.begin(), res.end()) << '\n';
  return 0;
}
