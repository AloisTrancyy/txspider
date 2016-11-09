/*
 Navicat Premium Data Transfer

 Source Server         : 10.168.66.173
 Source Server Type    : MySQL
 Source Server Version : 50625
 Source Host           : 10.168.66.173
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50625
 File Encoding         : utf-8

 Date: 11/09/2016 18:26:45 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `role`
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `role_id` varchar(11) DEFAULT NULL COMMENT '角色id',
  `role_name` varchar(255) DEFAULT NULL COMMENT '角色名',
  `role_url` varchar(255) DEFAULT NULL COMMENT '英雄榜链接',
  `role_level` int(2) DEFAULT NULL COMMENT '登记',
  `role_family` varchar(255) DEFAULT NULL COMMENT '势力',
  `role_school` int(2) DEFAULT NULL COMMENT '门派',
  `role_xiuwei` int(6) DEFAULT NULL COMMENT '人物修为',
  `role_eq` int(6) DEFAULT NULL COMMENT '装备评价',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
