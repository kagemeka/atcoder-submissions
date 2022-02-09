#include <bits/stdc++.h>
using namespace std;

int INF = 1001001001;
int n;
vector<int> abc(3);
vector<int> l(8);

int cost(vector<int> v, int c, int j) {
  if (j == n) {
    for (int i = 0; i < 3; i++) {
      if (!v[i]) return INF;
    }
    int ans = 10 * (c - 3);
    for (int i = 0; i < 3; i++) ans += abs(abc[i] - v[i]);
    return ans;
  }
  int ans = cost(v, c, j+1);
  for (int i = 0; i < 3; i++) {
    vector<int> nv = v;
    nv[i] += l[j];
    ans = min(ans, cost(nv, c+1, j+1));
  }
  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  for (int i = 0; i < 3; i++) cin >> abc[i];
  for (int i = 0; i < n; i++) cin >> l[i];
  cout << cost({0, 0, 0}, 0, 0) << '\n';
  return 0;
}
