#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
vector<int> Zalgo(const string &S) {
    int N = (int)S.size();
    vector<int> res(N);
    res[0] = N;
    int i = 1, j = 0;
    while (i < N) {
        while (i+j < N && S[j] == S[i+j]) ++j;
        res[i] = j;
        if (j == 0) {++i; continue;}
        int k = 1;
        while (i+k < N && k+res[k] < j) res[i+k] = res[k], ++k;
        i += k, j -= k;
    }
    return res;
}

int main() {
    int N;
    string S;
    cin >> N >> S;

    int res = 0;
    for (int i = 0; i < N; ++i) {
        string T = S.substr(i);
        auto lcp = Zalgo(T);

        for (int j = 0; j < T.size(); ++j) {
            int l = min(lcp[j], j);
            res = max(res, l);
        }
    }

    cout << res << endl;
}
