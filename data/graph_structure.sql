/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : graph_structure

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2019-11-18 20:21:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for attribute
-- ----------------------------
DROP TABLE IF EXISTS `attribute`;
CREATE TABLE `attribute` (
  `属性ID` varchar(255) NOT NULL,
  `属性名称` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`属性ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `品类ID` varchar(255) NOT NULL,
  `品类名称` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`品类ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for category_model
-- ----------------------------
DROP TABLE IF EXISTS `category_model`;
CREATE TABLE `category_model` (
  `品类ID` varchar(255) CHARACTER SET utf8 NOT NULL,
  `产品ID` varchar(255) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`品类ID`,`产品ID`),
  KEY `category_model_产品ID` (`产品ID`),
  CONSTRAINT `category_model_品类ID` FOREIGN KEY (`品类ID`) REFERENCES `category` (`品类ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `category_model_产品ID` FOREIGN KEY (`产品ID`) REFERENCES `model` (`产品ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` varchar(255) NOT NULL,
  `cid` int(11) DEFAULT NULL,
  `itemid` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `comment_all` varchar(255) DEFAULT NULL,
  `comment_date` datetime DEFAULT NULL,
  `datamonth` varchar(255) DEFAULT NULL,
  `comment_level` int(11) DEFAULT NULL,
  `commenter` varchar(255) DEFAULT NULL,
  `comment_url` varchar(255) DEFAULT NULL,
  `comment_pic` varchar(0) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `page` varchar(255) DEFAULT NULL,
  `seq` varchar(255) DEFAULT NULL,
  `version` varchar(255) DEFAULT NULL,
  `crawl_date` datetime DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for itemproperty
-- ----------------------------
DROP TABLE IF EXISTS `itemproperty`;
CREATE TABLE `itemproperty` (
  `cid` int(11) NOT NULL,
  `itemid` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `sku` varchar(255) DEFAULT NULL,
  `function` varchar(255) DEFAULT NULL,
  `sellernick` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `imageurl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for itemrecords
-- ----------------------------
DROP TABLE IF EXISTS `itemrecords`;
CREATE TABLE `itemrecords` (
  `cid` varchar(255) DEFAULT NULL,
  `itemid` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `biz30day` int(11) DEFAULT NULL,
  `total_sold_price` decimal(10,0) DEFAULT NULL,
  `comment_count` int(11) DEFAULT NULL,
  `advs` varchar(255) DEFAULT NULL,
  `disconnt` varchar(255) DEFAULT NULL,
  `datamonth` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for item_model
-- ----------------------------
DROP TABLE IF EXISTS `item_model`;
CREATE TABLE `item_model` (
  `cid` varchar(255) DEFAULT NULL,
  `itemid` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for model
-- ----------------------------
DROP TABLE IF EXISTS `model`;
CREATE TABLE `model` (
  `产品ID` varchar(255) NOT NULL,
  `品牌` varchar(255) DEFAULT NULL,
  `型号` varchar(255) DEFAULT NULL,
  `价格` decimal(10,2) DEFAULT NULL,
  `销售量` bigint(11) DEFAULT NULL,
  `销售额` decimal(10,2) DEFAULT NULL,
  `竞争力` decimal(10,2) DEFAULT NULL,
  `参数` varchar(255) DEFAULT NULL,
  `功能` varchar(255) DEFAULT NULL,
  `发布时间` varchar(255) DEFAULT NULL,
  `细分市场` varchar(255) DEFAULT NULL,
  `标题` varchar(255) DEFAULT NULL,
  `店铺` varchar(255) DEFAULT NULL,
  `促销` varchar(255) DEFAULT NULL,
  `热搜词` varchar(255) DEFAULT NULL,
  `图片链接` text,
  `商品链接` text,
  `好评率` decimal(10,0) DEFAULT NULL,
  `评价总数` int(255) DEFAULT NULL,
  PRIMARY KEY (`产品ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for modelproperty
-- ----------------------------
DROP TABLE IF EXISTS `modelproperty`;
CREATE TABLE `modelproperty` (
  `cid` int(11) NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `biz30day` int(255) DEFAULT NULL,
  `total_sold_price` decimal(10,0) DEFAULT NULL,
  `comment_count` int(11) DEFAULT NULL,
  `datamonth` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for modelrecords
-- ----------------------------
DROP TABLE IF EXISTS `modelrecords`;
CREATE TABLE `modelrecords` (
  `cid` int(11) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `biz30day` int(11) DEFAULT NULL,
  `total_sold_price` decimal(10,0) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `imageurl` varchar(255) DEFAULT NULL,
  `comment_count` varchar(255) DEFAULT NULL,
  `datamonth` varchar(255) DEFAULT NULL,
  `rate_ring_biz30day` int(11) DEFAULT NULL,
  `rate_ring_total_sold_price` decimal(10,0) DEFAULT NULL,
  `season_biz30day_raise` int(11) DEFAULT NULL,
  `season_total_sold_price_raise` int(11) DEFAULT NULL,
  `rate_year_biz30day` int(11) DEFAULT NULL,
  `rate_year_total_sold_price` int(11) DEFAULT NULL,
  `biz30day_increment` int(11) DEFAULT NULL,
  `total_sold_price_increment` decimal(10,0) DEFAULT NULL,
  `top_brand` varchar(255) DEFAULT NULL,
  `top_model` varchar(255) DEFAULT NULL,
  `top_ model_ratings` decimal(10,0) DEFAULT NULL,
  `model_ratings` decimal(10,0) DEFAULT NULL,
  `model_rank` varchar(255) DEFAULT NULL,
  `aver_model_ratings` decimal(10,0) DEFAULT NULL,
  `top_tag_ratings` varchar(0) DEFAULT NULL,
  `tag_ratings` varchar(0) DEFAULT NULL,
  `tag_rank` varchar(0) DEFAULT NULL,
  `aver_tag_ratings` varchar(0) DEFAULT NULL,
  `top_target_ratings` varchar(0) DEFAULT NULL,
  `target_ratings` varchar(0) DEFAULT NULL,
  `target_rank` varchar(0) DEFAULT NULL,
  `aver_target_ratings` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for model_attribute
-- ----------------------------
DROP TABLE IF EXISTS `model_attribute`;
CREATE TABLE `model_attribute` (
  `产品ID` varchar(255) CHARACTER SET utf8 NOT NULL,
  `属性ID` varchar(255) NOT NULL,
  `竞争力` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`产品ID`,`属性ID`),
  KEY `model_attribute_属性ID` (`属性ID`),
  CONSTRAINT `model_attribute_属性ID` FOREIGN KEY (`属性ID`) REFERENCES `attribute` (`属性ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `model_attribute_产品ID` FOREIGN KEY (`产品ID`) REFERENCES `model` (`产品ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for model_submerket
-- ----------------------------
DROP TABLE IF EXISTS `model_submerket`;
CREATE TABLE `model_submerket` (
  `cid` int(11) NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `submarketid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for source
-- ----------------------------
DROP TABLE IF EXISTS `source`;
CREATE TABLE `source` (
  `cid` int(11) NOT NULL,
  `source` varchar(255) DEFAULT NULL,
  `biz30day` int(255) DEFAULT NULL,
  `total_sold_price` decimal(10,0) DEFAULT NULL,
  `datamonth` varchar(255) DEFAULT NULL,
  `all_biz30day` varchar(255) DEFAULT NULL,
  `all_total_sold_price` decimal(10,0) DEFAULT NULL,
  `percent` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for submarket
-- ----------------------------
DROP TABLE IF EXISTS `submarket`;
CREATE TABLE `submarket` (
  `cid` varchar(255) DEFAULT NULL,
  `submarketid` varchar(255) DEFAULT NULL,
  `submarket` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for submarketrecords
-- ----------------------------
DROP TABLE IF EXISTS `submarketrecords`;
CREATE TABLE `submarketrecords` (
  `cid` int(11) DEFAULT NULL,
  `submarketID` varchar(255) DEFAULT NULL,
  `biz30day` int(11) DEFAULT NULL,
  `total_sold_price` decimal(10,0) DEFAULT NULL,
  `season_biz30day` int(11) DEFAULT NULL,
  `season_total_sold_price` decimal(10,0) DEFAULT NULL,
  `rate_season_biz30day` int(11) DEFAULT NULL,
  `rate_season_total_sold_price` decimal(10,0) DEFAULT NULL,
  `year_biz30day` int(11) DEFAULT NULL,
  `year_total_sold_price` decimal(10,0) DEFAULT NULL,
  `rate_year_biz30day` int(11) DEFAULT NULL,
  `rate_year_total_sold_price` decimal(10,0) DEFAULT NULL,
  `season_increase_biz30day` int(11) DEFAULT NULL,
  `season_increase_total_sold_price` decimal(10,0) DEFAULT NULL,
  `year_increase_biz30day` int(11) DEFAULT NULL,
  `year_increase_total_sold_price` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
