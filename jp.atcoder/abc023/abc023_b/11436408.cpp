#include <bits/stdc++.h>
using namespace std;

string make(int n) {

}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;

  if (n % 2 == 0) {
    cout << -1 << '\n';
    return 0;
  }

  int k = (n - 1) / 2;
  vector<char> res = {'b', 'c', 'a'};
  for (int i = 0; i < n; i++) {
    if (s[i] == res[(3-k%3+i)%3]) continue;
    cout << -1 << '\n';
    return 0;
  }
  cout << k << '\n';
  return 0;
}
