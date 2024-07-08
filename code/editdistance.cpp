#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int editDistance(string s, string t)
    {

        int len1 = s.size(), len2 = t.size();
        vector<vector<int>> dp(len1 + 1, vector<int>(len2 + 1, 0));

        for (int i = 0; i <= len1; i++)
            dp[i][0] = i;
        for (int i = 0; i <= len2; i++)
            dp[0][i] = i;
        for (int i = 1; i <= len1; i++)
        {
            for (int j = 1; j <= len2; j++)
            {
                if (s[i - 1] == t[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
            }
        }
        return dp[len1][len2];
    }
};

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        string s, t;
        cin >> s >> t;
        Solution ob;
        int ans = ob.editDistance(s, t);
        cout << ans << "\n";
    }
    return 0;
}