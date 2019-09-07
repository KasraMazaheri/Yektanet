#include "base_model.cpp"
using namespace std;
class Advertiser: public BaseAdvertising {
private:
    string name;
public:
    static int totalClicks;
    Advertiser(int _id = 0, string _name = "") {
        id = _id; name = _name;
    }
    string getName() {
        return (name);
    }
    void setName(string _name) {
        name = _name;
    }
    static int getTotalClicks() {
        return (totalClicks);
    }
    void incClicks() {
        clicks ++;
        totalClicks ++;
    }
    void incView() {
        views ++;
    }
    string describeMe() {
        return ("This class is meant to represent an advertiser.");
    }
   static string help() {
        return ("Here's a short description for each field of this class :\n\
                id: The id of this advertiser.\n\
                name: The name of the advertiser.\n\
                totalClicks: The total number of clicks that were made.\n\
                clicks: The number of clicks that were made on this advertiser's ads.\n\
                views: The number of times one of this advertiser's ads was viewed.");
    }
};
