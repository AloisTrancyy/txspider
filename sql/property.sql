/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-12-05 20:02:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for property
-- ----------------------------
DROP TABLE IF EXISTS `property`;
CREATE TABLE `property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prop_name` varchar(20) DEFAULT NULL,
  `prop_desc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of property
-- ----------------------------
INSERT INTO `property` VALUES ('5', 'jiahu', '加护值');
INSERT INTO `property` VALUES ('6', 'lianhu', '炼护值');
INSERT INTO `property` VALUES ('7', 'sex', '性别');
INSERT INTO `property` VALUES ('8', 'lv', '等级');
INSERT INTO `property` VALUES ('9', 'fly_soul_phase', '神启境界');
INSERT INTO `property` VALUES ('10', 'fly_soul_lv', '神启等级');
INSERT INTO `property` VALUES ('11', 'xiuwei', '人物修为');
INSERT INTO `property` VALUES ('12', 'equ_xiuwei', '装备评价');
INSERT INTO `property` VALUES ('13', 'sch', '门派');
INSERT INTO `property` VALUES ('14', 'mhp', '命');
INSERT INTO `property` VALUES ('15', 'msp', '技');
INSERT INTO `property` VALUES ('16', 'pattack_max', '最大物理攻击力');
INSERT INTO `property` VALUES ('17', 'mattack_max', '最大法术攻击力');
INSERT INTO `property` VALUES ('18', 'pattack_min', '最小物理攻击力');
INSERT INTO `property` VALUES ('19', 'mattack_min', '最小法术攻击力');
INSERT INTO `property` VALUES ('20', 'hit', '命中');
INSERT INTO `property` VALUES ('21', 'modadd', '重击');
INSERT INTO `property` VALUES ('22', 'critical', '会心一击');
INSERT INTO `property` VALUES ('23', 'attadd', '附伤');
INSERT INTO `property` VALUES ('24', 'cri_add_p', '诛心');
INSERT INTO `property` VALUES ('25', 'cri_sub_p', '御心');
INSERT INTO `property` VALUES ('26', 'mdef', '法术防御');
INSERT INTO `property` VALUES ('27', 'pdef', '物理防御');
INSERT INTO `property` VALUES ('28', 'absolutely_attack', '破阵');
INSERT INTO `property` VALUES ('29', 'absolutely_defence', '磐石');
INSERT INTO `property` VALUES ('30', 'inprotect', '神明');
INSERT INTO `property` VALUES ('31', 'avoid', '回避');
INSERT INTO `property` VALUES ('32', 'attdef', '化解');
INSERT INTO `property` VALUES ('33', 'defhuman', '知彼');
INSERT INTO `property` VALUES ('34', 'attackhuman', '人祸');
INSERT INTO `property` VALUES ('35', 'sract', '身份');
INSERT INTO `property` VALUES ('36', 'srbody', '坚韧');
INSERT INTO `property` VALUES ('37', 'srmind', '定力');
INSERT INTO `property` VALUES ('38', 'movespeed', '追电');
INSERT INTO `property` VALUES ('39', 'castspeed', '疾语');
INSERT INTO `property` VALUES ('40', 'attackspeed', '骤雨');
INSERT INTO `property` VALUES ('41', 'thump_add_p', '万钧');
INSERT INTO `property` VALUES ('42', 'thump_sub_p', '铁壁');
INSERT INTO `property` VALUES ('43', 'strong', '力');
INSERT INTO `property` VALUES ('44', 'body', '体');
INSERT INTO `property` VALUES ('45', 'quick', '敏');
INSERT INTO `property` VALUES ('46', 'dodge', '疾');
INSERT INTO `property` VALUES ('47', 'soul', '魂');
INSERT INTO `property` VALUES ('48', 'mind', '念');
INSERT INTO `property` VALUES ('86', 'mod_shui', '怒涛');
INSERT INTO `property` VALUES ('87', 'mod_feng', '狂风');
INSERT INTO `property` VALUES ('88', 'mod_du', '猛毒');
INSERT INTO `property` VALUES ('89', 'mod_huo', '爆炎');
INSERT INTO `property` VALUES ('90', 'mod_yuan', '真元');
INSERT INTO `property` VALUES ('91', 'mod_bairen', '白刃');
INSERT INTO `property` VALUES ('92', 'mod_dunci', '钝击');
INSERT INTO `property` VALUES ('93', 'mod_chuanci', '穿刺');
INSERT INTO `property` VALUES ('94', 'att_shui', '附加x点水伤害');
INSERT INTO `property` VALUES ('95', 'att_feng', '附加x点风伤害');
INSERT INTO `property` VALUES ('96', 'att_du', '附加x点毒伤害');
INSERT INTO `property` VALUES ('97', 'att_huo', '附加x点火伤害');
INSERT INTO `property` VALUES ('98', 'att_yuan', '附加x点元伤害');
INSERT INTO `property` VALUES ('99', 'def_shui', '御水');
INSERT INTO `property` VALUES ('100', 'def_feng', '御风');
INSERT INTO `property` VALUES ('101', 'def_du', '御毒');
INSERT INTO `property` VALUES ('102', 'def_huo', '御火');
INSERT INTO `property` VALUES ('103', 'def_yuan', '御元');
