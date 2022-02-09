#include <bits/stdc++.h>
using namespace std;

bool comp(tuple<string, int, int> &a, tuple<string, int, int> &b) {
  if (get<0>(a) == get<0>(b)) return get<1>(a) >= get<1>(b);
  else return get<0>(a) < get<0>(b);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<tuple<string, int, int>> res(n);
  for (int i = 0; i < n; i++) {
    string s;
    int p;
    cin >> s >> p;
    res[i] = make_tuple(s, p, i + 1);
  }
  sort(res.begin(), res.end(), comp);
  for (int i = 0; i < n; i++) {cout << get<2>(res[i]) << '\n';}
  return 0;
}
