#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string w;
  cin >> w;

  map<char, int> cnt;
  for (char &c : w) cnt[c]++;

  string ans = "Yes";
  for (auto &cv : cnt) {
    if (cv.second & 1) {
      ans = "No";
      break;
    }
  }
  cout << ans << '\n';
  return 0;

}
