#include <iostream>
#include <string>
#include <map>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;
  map<string, int> cnt;
  for (int i = 0; i < n; i++) {
    string s; cin >> s;
    cnt[s]++;
  }
  string ans = "";
  int c = 0;
  for (const auto &x : cnt) {
    if (x.second > c) {
      ans = x.first;
      c = x.second;
    }
  }

  cout << ans << '\n';
}
