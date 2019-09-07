#include "ad.cpp"
using namespace std;
int Advertiser::totalClicks = 0;
int main()
{
    BaseAdvertising baseAdvertising = BaseAdvertising();
    Advertiser advertiser1 = Advertiser(1, "name1");
    Advertiser advertiser2 = Advertiser(2, "name2");
    Ad ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1);
    Ad ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2);
    cout << baseAdvertising.describeMe() << "\n";
    cout << ad2.describeMe() << "\n";
    cout << advertiser1.describeMe () << "\n";
    ad1.incViews();
    ad1.incViews();
    ad1.incViews();
    ad1.incViews();
    ad2.incViews();
    ad1.incClicks();
    ad1.incClicks();
    ad2.incClicks();
    cout << advertiser2.getName() << "\n";
    advertiser2.setName("new name");
    cout << advertiser2.getName() << "\n";
    cout << ad1.getClicks() << "\n";
    cout << advertiser2.getClicks() << "\n";
    cout << Advertiser::getTotalClicks() << "\n";
    cout << Advertiser::help() << "\n";
}
