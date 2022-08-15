#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<string> s(n);
  for(int i = 0; i < n; i++) cin >> s[i];
  map<string, vector<string>> g;
  map<string, int> in_deg;
  for(auto& s: s) {
    int k = s.size();
    string u = s.substr(0, 3);
    string v = s.substr(k - 3, 3);
    g[v].push_back(u); // transpose
    in_deg[u]++;
  }
  queue<string> que;
  map<string, int> state;
  for(auto& [s, _]: g) {
    if(in_deg[s] == 0) {
      state[s] = 1;
      que.push(s);
    }
  }
  while(que.size()) {
    string u = que.front();
    que.pop();
    int su = state[u];
    for(auto& v: g[u]) {
      if(in_deg[v] == 0) continue;
      in_deg[v]--;
      if(su == 1) {
        state[v] = 2;
        in_deg[v] = 0;
        que.push(v);
      } else if(in_deg[v] == 0) {
        assert(su != 0);
        state[v] = 1;
        que.push(v);
      }
    }
  }
  for(auto& s: s) {
    int k = s.size();
    string u = s.substr(k - 3, 3);
    int su = state[u];
    if(su == 0) {
      cout << "Draw";
    } else if(su == 2) {
      cout << "Aoki";
    } else {
      cout << "Takahashi";
    }
    cout << '\n';
  }
}
