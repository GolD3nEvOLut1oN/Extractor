/*
Navicat MySQL Data Transfer

Source Server         : AWS BD Falabella
Source Server Version : 50637
Source Host           : falabella-instance.cp9klnmuospb.us-east-2.rds.amazonaws.com:3306
Source Database       : falabella

Target Server Type    : MYSQL
Target Server Version : 50637
File Encoding         : 65001

Date: 2018-03-11 21:44:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ripley
-- ----------------------------
DROP TABLE IF EXISTS `ripley`;
CREATE TABLE `ripley` (
  `bprice` bigint(20) DEFAULT NULL,
  `cat_url` varchar(400) COLLATE utf8_spanish_ci DEFAULT NULL,
  `category` varchar(400) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cprice` bigint(20) DEFAULT NULL,
  `name` varchar(400) COLLATE utf8_spanish_ci DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL,
  `up_category` varchar(400) COLLATE utf8_spanish_ci DEFAULT NULL,
  `up_category_url` varchar(400) COLLATE utf8_spanish_ci DEFAULT NULL,
  `url` varchar(400) COLLATE utf8_spanish_ci DEFAULT NULL,
  KEY `bprice` (`bprice`,`cprice`,`name`(255),`price`),
  KEY `name` (`name`(255),`url`(255)),
  KEY `url` (`url`(255)),
  KEY `nameprice` (`name`(255),`price`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
