/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-11-09 22:55:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for role_atk
-- ----------------------------
DROP TABLE IF EXISTS `role_atk`;
CREATE TABLE `role_atk` (
  `id` bigint(20) NOT NULL,
  `role_id` varchar(10) NOT NULL,
  `maxad` int(5) NOT NULL DEFAULT '0',
  `minad` int(5) NOT NULL DEFAULT '0',
  `maxma` int(5) NOT NULL DEFAULT '0',
  `minma` int(5) NOT NULL DEFAULT '0',
  `minzhong` int(5) NOT NULL DEFAULT '0',
  `zhongji` int(5) NOT NULL DEFAULT '0',
  `huixin` int(5) NOT NULL DEFAULT '0',
  `fushang` int(5) NOT NULL DEFAULT '0',
  `renhuo` int(2) NOT NULL DEFAULT '0',
  `wanjun` int(3) NOT NULL DEFAULT '0',
  `tiebi` int(3) NOT NULL DEFAULT '0',
  `zhuxin` int(2) NOT NULL DEFAULT '0',
  `yuxin` int(2) NOT NULL DEFAULT '0',
  `zhuidian` int(2) NOT NULL DEFAULT '0',
  `jiyu` int(2) NOT NULL DEFAULT '0',
  `shenfa` int(2) NOT NULL DEFAULT '0',
  `jianren` int(2) NOT NULL DEFAULT '0',
  `dingli` int(2) NOT NULL DEFAULT '0',
  `fangyu` int(2) NOT NULL DEFAULT '0',
  `huibi` int(2) NOT NULL DEFAULT '0',
  `fafang` int(2) NOT NULL DEFAULT '0',
  `shenming` int(2) NOT NULL DEFAULT '0',
  `huajie` int(2) NOT NULL DEFAULT '0',
  `zhibi` int(2) NOT NULL DEFAULT '0',
  `pozhen` int(3) NOT NULL DEFAULT '0',
  `panshi` int(3) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_basic
-- ----------------------------
DROP TABLE IF EXISTS `role_basic`;
CREATE TABLE `role_basic` (
  `id` bigint(20) NOT NULL,
  `role_id` varchar(10) NOT NULL,
  `jiahu` int(3) NOT NULL DEFAULT '0',
  `lianhu` int(3) NOT NULL DEFAULT '0',
  `rmb` int(6) NOT NULL DEFAULT '80',
  `name` varchar(30) DEFAULT NULL,
  `level` varchar(20) DEFAULT NULL,
  `school` varchar(10) DEFAULT NULL,
  `server` varchar(10) DEFAULT NULL,
  `family` varchar(50) DEFAULT NULL,
  `hp` int(5) NOT NULL DEFAULT '0',
  `mp` int(5) NOT NULL DEFAULT '0',
  `li` int(4) NOT NULL DEFAULT '0',
  `ti` int(4) NOT NULL DEFAULT '0',
  `min` int(4) NOT NULL DEFAULT '0',
  `ji` int(4) NOT NULL DEFAULT '0',
  `hun` int(4) NOT NULL DEFAULT '0',
  `nian` int(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`),
  KEY `idx_rmb` (`rmb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_def
-- ----------------------------
DROP TABLE IF EXISTS `role_def`;
CREATE TABLE `role_def` (
  `id` bigint(20) NOT NULL,
  `role_id` varchar(10) NOT NULL,
  `zhanchang` int(2) NOT NULL DEFAULT '0',
  `dayu` int(3) NOT NULL DEFAULT '0',
  `junzi` int(2) NOT NULL DEFAULT '0',
  `tianyu` int(2) NOT NULL DEFAULT '0',
  `jjc` int(2) NOT NULL DEFAULT '0',
  `liuyao` int(2) NOT NULL DEFAULT '0',
  `yuanbao` int(2) NOT NULL DEFAULT '0',
  `jinbi` int(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_haizi
-- ----------------------------
DROP TABLE IF EXISTS `role_haizi`;
CREATE TABLE `role_haizi` (
  `id` bigint(20) NOT NULL,
  `role_id`  varchar(10) NOT NULL,
  `level` int(2) NOT NULL DEFAULT '0',
  `school` varchar(30) NOT NULL,
  `wuxue` int(2) NOT NULL DEFAULT '0',
  `zizhi` int(4) NOT NULL DEFAULT '0',
  `xueshi` int(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_jineng
-- ----------------------------
DROP TABLE IF EXISTS `role_jineng`;
CREATE TABLE `role_jineng` (
  `id` bigint(20) NOT NULL,
  `role_id`  varchar(10) NOT NULL,
  `fujin` tinyint(1) NOT NULL DEFAULT '0',
  `yanzi` tinyint(1) NOT NULL DEFAULT '0',
  `qingting` tinyint(1) NOT NULL DEFAULT '0',
  `taxue` tinyint(1) NOT NULL DEFAULT '0',
  `feiyan` tinyint(1) NOT NULL DEFAULT '0',
  `xueji` tinyint(1) NOT NULL DEFAULT '0',
  `paoxiao` tinyint(1) NOT NULL DEFAULT '0',
  `shalu`  tinyint(1) NOT NULL DEFAULT '0',
  `menpai` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_juexing
-- ----------------------------
DROP TABLE IF EXISTS `role_juexing`;
CREATE TABLE `role_juexing` (
  `id` bigint(20) NOT NULL,
  `role_id`  varchar(10) NOT NULL,
  `level` tinyint(1) NOT NULL DEFAULT '0',
  `fengjinzhili` tinyint(2) NOT NULL DEFAULT '0',
  `juexingdu` int(2) NOT NULL DEFAULT '0',
  `liandao` int(4) NOT NULL DEFAULT '0',
  `lianhu` int(3) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_shizhuang
-- ----------------------------
DROP TABLE IF EXISTS `role_shizhuang`;
CREATE TABLE `role_shizhuang` (
  `id` bigint(20) NOT NULL,
  `role_id`  varchar(10) NOT NULL,
  `dairanqinghua` tinyint(1) NOT NULL DEFAULT '0',
  `xuansutiancheng` tinyint(1) NOT NULL DEFAULT '0',
  `guhongyueying` tinyint(1) NOT NULL DEFAULT '0',
  `xiangyunsinuan` tinyint(1) NOT NULL DEFAULT '0',
  `anchitinglan` tinyint(1) NOT NULL DEFAULT '0',
  `haitangweiyu` tinyint(1) NOT NULL DEFAULT '0',
  `feihuhuaqiu` tinyint(1) NOT NULL DEFAULT '0',
  `tianhulishang` tinyint(1) NOT NULL DEFAULT '0',
  `xianhucaijue` tinyint(1) NOT NULL DEFAULT '0',
  `dashengjinjia` tinyint(1) NOT NULL DEFAULT '0',
  `canghaisangtian` tinyint(1) NOT NULL DEFAULT '0',
  `yeyujiangnan` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_teji
-- ----------------------------
DROP TABLE IF EXISTS `role_teji`;
CREATE TABLE `role_teji` (
  `id` bigint(20) NOT NULL,
  `role_id`  varchar(10) NOT NULL,
  `huikanjingtong` tinyint(1) NOT NULL DEFAULT '0',
  `chuancijingtong` tinyint(1) NOT NULL DEFAULT '0',
  `dunjijingtong` tinyint(1) NOT NULL DEFAULT '0',
  `huikanfanghu` tinyint(1) NOT NULL DEFAULT '0',
  `duncifanghu` tinyint(1) NOT NULL DEFAULT '0',
  `huoyuanfanghu` tinyint(1) NOT NULL DEFAULT '0',
  `shuifengdufanghu` tinyint(1) NOT NULL DEFAULT '0',
  `wanfeng` tinyint(1) NOT NULL DEFAULT '0',
  `huxin` tinyint(1) NOT NULL DEFAULT '0',
  `dayushenyou` tinyint(1) NOT NULL DEFAULT '0',
  `dayulongfei` tinyint(1) NOT NULL DEFAULT '0',
  `dayutianfei` tinyint(1) NOT NULL DEFAULT '0',
  `douzhuanbian` tinyint(1) NOT NULL DEFAULT '0',
  `yixinghuanying` tinyint(1) NOT NULL DEFAULT '0',
  `menpaiteji` tinyint(1) NOT NULL DEFAULT '0',
  `taichu` tinyint(1) NOT NULL DEFAULT '0',
  `shilifushou` tinyint(1) NOT NULL DEFAULT '0',
  `menpaifushou` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for role_zhuzi
-- ----------------------------
DROP TABLE IF EXISTS `role_zhuzi`;
CREATE TABLE `role_zhuzi` (
  `id` bigint(20) NOT NULL,
  `role_id`  varchar(10) NOT NULL,
  `shibing` tinyint(1) NOT NULL DEFAULT '0',
  `shenqi` tinyint(1) NOT NULL DEFAULT '0',
  `zhumu` tinyint(1) NOT NULL DEFAULT '0',
  `xianhu` tinyint(1) NOT NULL DEFAULT '0',
  `shuisheng` tinyint(1) NOT NULL DEFAULT '0',
  `youxiong` tinyint(1) NOT NULL DEFAULT '0',
  `linghou` tinyint(1) NOT NULL DEFAULT '0',
  `qiangdao` tinyint(1) NOT NULL DEFAULT '0',
  `menghu` tinyint(1) NOT NULL DEFAULT '0',
  `huacao` tinyint(1) NOT NULL DEFAULT '0',
  `ligui` tinyint(1) NOT NULL DEFAULT '0',
  `xiyangyang` tinyint(1) NOT NULL DEFAULT '0',
  `mawangye` tinyint(1) NOT NULL DEFAULT '0',
  `wangshengtianzun` tinyint(1) NOT NULL DEFAULT '0',
  `yehuo` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
