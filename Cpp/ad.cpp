#include "advertiser.cpp"
using namespace std;
class Ad: public BaseAdvertising {
private:
    string title, imgUrl, link;
    Advertiser * advertiser;
public:
    Ad(int _id, string _title, string _imgUrl, string _link, Advertiser &_advertiser) {
        id = _id; title = _title; imgUrl = _imgUrl; link = _link; advertiser = &_advertiser;
    }
    string getTitle() {
        return (title);
    }
    void setTitle(string _title) {
        title = _title;
    }
    string getImgUrl() {
        return (imgUrl);
    }
    void setImgUrl(string _imgUrl) {
        imgUrl = _imgUrl;
    }
    string getLink() {
        return (link);
    }
    void setLink(string _link) {
        link = _link;
    }
    void setAdvertiser(Advertiser &_advertiser) {
        advertiser = &_advertiser;
    }
    void incClicks() {
        clicks ++;
        advertiser->incClicks();
    }
    void incViews() {
        views ++;
        advertiser->incViews();
    }
    string describeMe() {
        return ("This class is meant to represent an ad.");
    }
};
