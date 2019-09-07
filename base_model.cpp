// ItnoE
#include<bits/stdc++.h>
using namespace std;
class BaseAdvertising {
protected :
    int id = 0, clicks = 0, views = 0;
public:
    BaseAdvertising() {}
    int getClicks() {
        return (clicks);
    }
    int getViews() {
        return (views);
    }
    void incClicks() {}
    void incViews() {}
    string describeMe() {
        return ("This class is the base of our other classes.");
    }
};
