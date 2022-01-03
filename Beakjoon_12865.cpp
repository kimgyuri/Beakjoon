// DP
#include <iostream>
#include <string>
#include<algorithm>
using namespace std;

// N : 물품 수
// K : 버틸 수 있는 무게
// W : 물건 무게
// V : 물건 가치
int N, K, W, V;
int Items[101][2];
int dp[101][100001];


int main() {

    cin >> N >> K;

    for (int i=1; i<=N; i++) {
        cin >> W >> V;
        Items[i][0] = W;
        Items[i][1] = V;

        for(int j=0; j<=K; j++) {
            if (j < Items[i][0]) {
                dp[i][j] = dp[i-1][j];
            }
            else {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V);
            }
        }
    }
    
    cout << dp[N][K] << endl;

}