#include<stdio.h>
#include <algorithm>

using namespace std;

typedef long long ll;
const int MAX_M = 15;

int M = 3, X = 600000;
double P = 0.75;

double dp[2][(1 << MAX_M) + 1];

void solve() {
    // n = 2^M
    int n = 1 << M;

    double *prv = dp[0], *nxt = dp[1];
    memset(prv, 0, sizeof(double) * (n + 1));
    // 既に100万円持っていれば確率1
    prv[n] = 1.0;

    for (int r = 0; r < M; r++) {
        for (int i = 0; i <= n; i++) {
            int jub = min(i, n - i);
            printf("%d\n",n);
            double t = 0.0;
            for (int j = 0; j <= jub; j++) {
                // printf("%d,%d,%d,%d\n",r,i,j,jub*125000);
                t = max(t, P * prv[i + j] + (1 - P) * prv[i - j]);
            }
            nxt[i] = t;
        }
        swap(prv, nxt);
        printf("1 term\n");
        for(int k = 0; k <=n; k++){
            printf("%.6f\n", prv[k]);
        }
    }

    // 全勝した場合の金額 / 100万円
    int i = (ll)X * n / 1000000;
}

int main(void){
    solve();
}