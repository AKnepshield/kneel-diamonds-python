DELETE FROM Metals;
DELETE FROM Styles;
DELETE FROM Sizes;
DElETE FROM Orders;

DROP TABLE IF EXISTS Metals;
DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Orders;


CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

INSERT INTO `Metals` VALUES(NULL, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES(NULL, "14K Gold", 736.4);
INSERT INTO `Metals` VALUES(NULL, "24K Gold", 1258.9);
INSERT INTO `Metals` VALUES(NULL, "Platinum", 795.45);
INSERT INTO `Metals` VALUES(NULL, "Palladium", 1241);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC (160) NOT NULL,
    `price` NUMERIC (5,2) NOT NULL
);

INSERT INTO `Sizes` VALUES(NULL, .5, 405);
INSERT INTO `Sizes` VALUES(NULL, .75, 782);
INSERT INTO `Sizes` VALUES(NULL, 1, 1470);
INSERT INTO `Sizes` VALUES(NULL, 1.5, 1997);
INSERT INTO `Sizes` VALUES(NULL, 2, 3638);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

INSERT INTO `Styles` VALUES(NULL, "Classic", 500);
INSERT INTO `Styles` VALUES(NULL, "Modern", 710);
INSERT INTO `Styles` VALUES(NULL, "Vintage", 965);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `metal_id` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`)
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`)
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO `Orders` VALUES(NULL, 1, 1, 1);
INSERT INTO `Orders` VALUES(NULL, 2, 2, 2);
INSERT INTO `Orders` VALUES(NULL, 3, 3, 3);

