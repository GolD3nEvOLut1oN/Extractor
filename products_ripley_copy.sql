/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : ripley

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2017-11-13 04:14:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for paris
-- ----------------------------
DROP TABLE IF EXISTS `paris`;
CREATE TABLE `paris` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `img_url` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `name` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `price` bigint(15) DEFAULT NULL,
  `bprice` bigint(15) DEFAULT NULL,
  `cprice` bigint(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `category` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prices` (`name`,`price`,`bprice`,`cprice`),
  KEY `idx_name` (`url`,`name`),
  KEY `idx_url_only` (`url`),
  KEY `idx_date_price` (`name`,`price`,`bprice`,`cprice`,`date`)
) ENGINE=InnoDB AUTO_INCREMENT=204168 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
