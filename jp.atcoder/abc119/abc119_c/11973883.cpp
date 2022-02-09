#include <bits/stdc++.h>
using namespace std;

queue<string> res;
void product(string cand, int repeat) {
  auto now = res.front();
  if (now.size() == repeat) return;
  res.pop();
  for (auto &c : cand) res.push(now + c);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, a, b, c;
  cin >> n >> a >> b >> c;
  vector<int> abc = {0, a, b, c};
  vector<int> l(n);
  for (int i = 0; i < n; i++) cin >> l[i];

  string cand = "0123";
  queue<string> res;
  res.push("");
  while (res.front().size() != n) {
    string now = res.front(); res.pop();
    for (auto &c : cand) res.push(now + c);
  }
  vector<int> ans;
  while (!res.empty()) {
    auto p = res.front(); res.pop();
    vector<vector<int>> group(4);
    for (int i = 0; i < n; i++) {
      group[p[i]-'0'].push_back(l[i]);
    }
    int cost = 0;
    bool flag = true;
    for (int i = 1; i < 4; i++) {
      if (group[i].size() == 0) {flag = false; break;}
      cost += 10 * (group[i].size() - 1);
      int s = accumulate(group[i].begin(), group[i].end(), 0);
      cost += abs(s - abc[i]);
    }
    if (flag) ans.push_back(cost);
  }
  cout << *min_element(ans.begin(), ans.end()) << '\n';
  return 0;
}
