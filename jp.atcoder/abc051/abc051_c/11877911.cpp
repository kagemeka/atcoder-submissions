#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d;
  cin >> a >> b >> c >> d;
  int dy = d - b;
  int dx = c - a;
  string res = "";
  for (int i = 0; i < dy; i++) res += "U";
  for (int i = 0; i < dx + 1; i++) res += "R";
  for (int i = 0; i < dy + 1; i++) res += "D";
  for (int i = 0; i < dx; i++) res += "L";
  for (int i = 0; i < 1; i++) res += "U";
  for (int i = 0; i < 1; i++) res += "L";
  for (int i = 0; i < dy + 1; i++) res += "U";
  for (int i = 0; i < dx + 1; i++) res += "R";
  for (int i = 0; i < dy + 1; i++) res += "D";
  for (int i = 0; i < dy; i++) res += "L";
  cout << res << '\n';
  return 0;
}
