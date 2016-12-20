/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-12-20 15:53:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for car_resource_detail
-- ----------------------------
DROP TABLE IF EXISTS `car_resource_detail`;
CREATE TABLE `car_resource_detail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `res_id` bigint(20) NOT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `brand_name` varchar(30) DEFAULT NULL,
  `spec_name` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `car_config` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `car_type` tinyint(1) NOT NULL COMMENT '1国产2中规3美规4中东5加版6欧版',
  `car_status` varchar(100) DEFAULT '1' COMMENT '1现车',
  `sale_area` varchar(255) DEFAULT NULL,
  `node` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of car_resource_detail
-- ----------------------------
