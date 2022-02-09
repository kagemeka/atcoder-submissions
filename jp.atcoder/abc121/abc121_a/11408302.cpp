#include <bits/stdc++.h>
using namespace std;

int main() {
  int H, W, h, w;
  cin >> H >> W >> h >> w;
  int s = H * W - (H*w + h*W - h*w);
  cout << s << endl;
  return 0;
}
