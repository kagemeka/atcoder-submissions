#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>

using namespace std;


namespace GeometryTopology {
  template<typename T>
  double triangle_area(pair<T, T> p0, pair<T, T> p1, pair<T, T> p2, bool sign=true) {
    T x0 = p1.first - p0.first;
    T x1 = p2.first - p0.first;
    T y0 = p1.second - p0.second;
    T y1 = p2.second - p0.second;
    double s = (x0*y1 - x1*y0) / 2.0;
    if (sign) {return s;}
    return abs(s);
  }
}

using namespace GeometryTopology;

namespace AtCoder {

namespace ABC001 {
void a() {int a, b; cin >> a >> b; cout << a-b << '\n';}
void b() {}
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

void c() {
  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;
  pair<int, int> p0, p1, p2;
  p0 = make_pair(a, b);
  p1 = make_pair(c, d);
  p2 = make_pair(e, f);
  auto s = triangle_area(p0, p1, p2, false);
  cout << setprecision(16)  << s <<'\n';
}

void d() {
  int n, m; cin >> n >> m;
  vector<int> relations(n, 0);
  for (int i = 0; i < m; i++) {
    int x, y; cin >> x >> y; x--; y--;
    relations[x] |= 1<<y; relations[y] |= 1<<x;
  }
  int res = 0;
  for (int i = 0; i < 1<<n; i++) {
    int s = (1<<n) - 1, cnt = 0;
    for (int j = 0; j < n; j++) {
      if (i>>j&1) {s &= relations[j] | 1<<j; cnt++;}
    }
    if ((s&i)==i) {res = max(res, cnt);}
  }
  cout << res << '\n';
}
}



}

namespace Codeforces {
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);


  AtCoder::ABC002::d();


  return 0;

}
