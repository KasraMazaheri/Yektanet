CREATE DATABASE AdvertisingSystem
SELECT AdvertisingSystem

CREATE TABLE Advertiser {
	id int not null,
	name varchar(100) not null,
	clicks int default 0,
	views int default 0,
	PRIMARY KEY (id)
};

CREATE TABLE Ad {
	id int not null,
	title varchar(100) not null,
	imgUrl varchar(100) not null,
	link varchar(100) not null,
	advertiser_id int REFERENCES Advertiser(id) not null,
	clicks int default 0,
	views int default 0,
	PRIMARY KEY (id)
};

INSERT INTO Advertiser VALUES (1, "name1")
INSERT INTO Advertiser VALUES (2, "name2")

INSERT INTO Ad VALUES (1, "title1", "img-url1", "link1", 1)
INSERT INTO Ad VALUES (2, "title2", "img-url2", "link2", 2)
