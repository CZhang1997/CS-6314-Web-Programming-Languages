
create database FavoritePlaces;
use FavoritePlaces;
CREATE TABLE `Restaurants` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name` VARCHAR( 60 ) NOT NULL ,
  `address` VARCHAR( 80 ) NOT NULL ,
  `lat` FLOAT( 10, 6 ) NOT NULL ,
  `lng` FLOAT( 10, 6 ) NOT NULL ,
  `type` VARCHAR( 30 ) NOT NULL
) ENGINE = MYISAM ;

INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Lucky City", "3215 Independence Pkwy, Plano, TX 75075, USA", 33.0397033,-96.7542972, "restaurant");
INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Mudleaf Coffee", "3100 Independence Pkwy #300, Plano, TX 75075, USA", 33.0406858,-96.75085820000001, "cafe");
INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Bull Daddy Noodle Bistro", "3309 Coit Rd #100, Plano, TX 75093, USA", 33.0425785,-96.7705574, "restaurant");
INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("East Wall Chinese Cuisine", "3033 W Parker Rd #214, Plano, TX 75023, USA", 33.0425315,-96.7526559, "restaurant");
INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Olive Burger Plano", "2129 W Parker Rd #301, Plano, TX 75023, USA", 33.0429329,-96.733908, "restaurant");
INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("First Chinese BBQ Plano", "3304 Coit Rd, Plano, TX 75023, USA", 33.04231600000001,-96.76936099999999, "restaurant");
INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("King Buffet Plano", "521 E Central Pkwy, Plano, TX 75074, USA", 33.026728,-96.708162, "restaurant");
