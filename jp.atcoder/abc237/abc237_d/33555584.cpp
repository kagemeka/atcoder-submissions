#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  deque<int> dq;
  bool zero_left = true;
  if(n > 1 && s[0] == 'L') zero_left = false;
  dq.push_front(0);
  for(int i = 0; i < n; i++) {
    if(s[i] == 'R') {
      dq.push_back(dq.front());
      dq.pop_front();
    }
    dq.push_front(i + 1);
  }
  while(dq.front() != 0) {
    dq.push_back(dq.front());
    dq.pop_front();
  }
  if(!zero_left) {
    dq.push_back(dq.front());
    dq.pop_front();
  }
  for(int i = 0; i < n + 1; i++) {
    cout << dq.front() << " \n"[i == n];
    dq.pop_front();
  }
}
