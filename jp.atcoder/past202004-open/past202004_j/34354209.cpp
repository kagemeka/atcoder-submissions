#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  stack<string> st;
  for(auto& c: s) {
    if(st.empty()) {
      st.push(string(1, c));
      continue;
    }
    if(c == '(') {
      st.push("(");
      continue;
    }
    if(c == ')') {
      if(st.top() == "(") {
        st.pop();
      } else {
        string t = st.top();
        st.pop();
        assert(st.top() == "(");
        st.pop();
        string tt = t;
        reverse(tt.begin(), tt.end());
        if(st.empty() || st.top() == "(") {
          st.push(t + tt);
        } else {
          st.top() += t + tt;
        }
      }
      continue;
    }
    if(st.top() == "(") {
      st.push(string(1, c));
    } else {
      st.top() += c;
    }
  }
  assert(st.size() == 1);
  cout << st.top() << endl;
}
