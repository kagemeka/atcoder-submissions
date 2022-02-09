#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>

using namespace std;


namespace AtCoder {
  namespace ABC001 {
    void a() {
      int a, b; cin >> a >> b;
      cout << a-b << '\n';
    }
    void b() {

    }
  }
  namespace ABC002 {
    void a() {
      int x, y; cin >> x >> y;
      cout << max(x, y) << '\n';
    }

    void b() {
      set<char> vowels;
      for (auto &c : "aeiou") {vowels.insert(c);}
      string w;
      cin >> w;
      string s = "";
      for (char &c : w) {
        if (vowels.count(c)) {continue;}
        s += c;
      }
      cout << s << '\n';
    }
  }
}

namespace Codeforces {
  namespace ABC001 {
    void a() {
    }
  }
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);


  AtCoder::ABC002::b();


  return 0;

}
