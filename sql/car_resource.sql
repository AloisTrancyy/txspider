/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-12-20 15:53:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for car_resource
-- ----------------------------
DROP TABLE IF EXISTS `car_resource`;
CREATE TABLE `car_resource` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `res_source` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1车行168 2车源宝',
  `uid` varchar(100) NOT NULL,
  `res_name` varchar(255) DEFAULT NULL,
  `res_type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '资源类型1个人 2公司',
  `city_id` int(11) DEFAULT NULL,
  `city_name` varchar(255) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL COMMENT '联系方式',
  `fresh_time` datetime DEFAULT NULL,
  `detail_url` varchar(255) DEFAULT NULL,
  `craw` tinyint(1) NOT NULL DEFAULT '0',
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of car_resource
-- ----------------------------
INSERT INTO `car_resource` VALUES ('1', '1', 'uutze_107297', '天津纵横伟业宾利专卖资源表', '1', null, '天津', null, '2016-12-20 10:36:00', '/index.php?c=com&m=zyInfo&uid=uutze_107297', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('2', '1', 'iliwk_25621', '天津疆越国际资源表', '1', null, '天津', null, '2016-12-20 10:36:00', '/index.php?c=com&m=zyInfo&uid=iliwk_25621', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('3', '1', 'hevfj_6558', '天津世鑫国际资源表', '1', null, '天津', null, '2016-12-20 10:36:00', '/index.php?c=com&m=zyInfo&uid=hevfj_6558', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('4', '1', 'njcbq_38726', '天津鑫昌通汽贸资源表', '1', null, '天津', null, '2016-12-20 10:36:00', '/index.php?c=com&m=zyInfo&uid=njcbq_38726', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('5', '1', 'fsiuo_3430', '天津保路驰资源表', '1', null, '天津', null, '2016-12-20 10:36:00', '/index.php?c=com&m=zyInfo&uid=fsiuo_3430', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('6', '1', 'xjkjb_189239', '天津佰瑞特资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=xjkjb_189239', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('7', '1', 'ksurk_23432', '北京菲弘汽车资源表', '1', null, '北京', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=ksurk_23432', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('8', '1', 'tczer_217125', '天津宝隆兴业资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=tczer_217125', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('9', '1', 'zydiw_14483', '北京祥辉奥通资源表', '1', null, '北京', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=zydiw_14483', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('10', '1', 'xwnpp_67230', '天津爱车空间资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=xwnpp_67230', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('11', '1', 'zpfmf_129738', '天津盛世源奔驰专卖资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=zpfmf_129738', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('12', '1', 'aildf_165525', '天津欧美加野马专卖资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=aildf_165525', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('13', '1', 'ukify_1717', '大连峰尚轩资源表', '1', null, '辽宁', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=ukify_1717', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('14', '1', 'hzcgz_5590', '天津东巨奔驰专卖资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=hzcgz_5590', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('15', '1', 'bpnhh_2001', '天津欣瑞德资源表', '1', null, '北京', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=bpnhh_2001', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('16', '1', 'zhggt_43465', '天津嘉跃行资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=zhggt_43465', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('17', '1', 'mxybc_5451', '天津众旺汽车资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=mxybc_5451', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('18', '1', 'cgajw_217', '天津鼎程奔驰专卖资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=cgajw_217', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('19', '1', 'sdbyz_5580', '天津世之贸资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=sdbyz_5580', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('20', '1', 'joxuf_12746', '天津大元国际资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=joxuf_12746', '0', '2016-12-20 10:49:24');
INSERT INTO `car_resource` VALUES ('21', '1', 'oncsf_21490', '林丛个人资源表', '1', null, '吉林', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=oncsf_21490', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('22', '1', 'ygmke_32799', '李阳个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=ygmke_32799', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('23', '1', 'jgwsh_9680', '肖文斌个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=jgwsh_9680', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('24', '1', 'kxhii_7955', '宁飚然个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=kxhii_7955', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('25', '1', 'oziim_179090', '王晓晨个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=oziim_179090', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('26', '1', 'jdvue_87370', '顾劲枫个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=jdvue_87370', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('27', '1', 'sdezl_36644', '龚贤忠个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=sdezl_36644', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('28', '1', 'ttapm_8230', '张万金个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=ttapm_8230', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('29', '1', 'kjgxp_136670', '董金昊个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=kjgxp_136670', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('30', '1', 'bvmuo_147866', '王玉兰个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=bvmuo_147866', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('31', '1', 'oipwt_146175', '刘绪玲个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=oipwt_146175', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('32', '1', 'vbmuo_113007', '武刚个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=vbmuo_113007', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('33', '1', 'tcdva_137985', '曹卫春个人资源表', '1', null, '北京', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=tcdva_137985', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('34', '1', 'sglxz_192761', '桑艳丽个人资源表', '1', null, '河南', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=sglxz_192761', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('35', '1', 'hnhhh_72969', '凌菲个人资源表', '1', null, '上海', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=hnhhh_72969', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('36', '1', 'rsceg_154329', '牟楠个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=rsceg_154329', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('37', '1', 'jalec_212566', '王亮个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=jalec_212566', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('38', '1', 'vyyaw_112329', '陈峙芳个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=vyyaw_112329', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('39', '1', 'dgevp_184636', '阿衣金洛个人资源表', '1', null, '北京', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=dgevp_184636', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('40', '1', 'bhvdr_11861', '叶俊个人资源表', '1', null, '上海', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=bhvdr_11861', '0', '2016-12-20 10:49:28');
INSERT INTO `car_resource` VALUES ('41', '1', 'dixng_145575', '北京扬帆晟诚汽车资源表', '1', null, '黑龙江', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=dixng_145575', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('42', '1', 'uhauc_9221', '北京继东汽车资源表', '1', null, '北京', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=uhauc_9221', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('43', '1', 'ymrlx_85091', '天津路盛汽车贸易有限公司资源表', '1', null, '天津', null, '2016-12-20 10:35:00', '/index.php?c=com&m=zyInfo&uid=ymrlx_85091', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('44', '1', 'qcjck_6615', '天津车之速汽车资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=qcjck_6615', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('45', '1', 'wyzb_35506', '万源众邦控股(集团)资源表', '1', null, '北京', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=wyzb_35506', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('46', '1', 'sxvlw_72241', '天津鹏都国际贸易资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=sxvlw_72241', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('47', '1', 'ykjij_6158', '万源众邦（天津）综合资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=ykjij_6158', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('48', '1', 'ktnrx_29380', '天津大鑫源资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=ktnrx_29380', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('49', '1', 'rzsbd_33094', '天津永大百运佳路虎专卖资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=rzsbd_33094', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('50', '1', 'tysxd_78238', '天津裕鼎汽车资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=tysxd_78238', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('51', '1', 'lrojr_101241', '青岛安华机电奔驰专卖资源表', '1', null, '山东', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=lrojr_101241', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('52', '1', 'puoxy_132526', '天津诚而信资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=puoxy_132526', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('53', '1', 'rvmro_51363', '青岛安华机电资源表', '1', null, '山东', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=rvmro_51363', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('54', '1', 'pxjwr_49376', '天津荣冶林资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=pxjwr_49376', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('55', '1', 'sinpt_1857', '天津华夏安邦资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=sinpt_1857', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('56', '1', 'dzwkg_52763', '北京亚鑫通达资源表', '1', null, '北京', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=dzwkg_52763', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('57', '1', 'kbbbk_39324', '天津起越天成资源表', '1', null, '天津', null, '2016-12-20 10:34:00', '/index.php?c=com&m=zyInfo&uid=kbbbk_39324', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('58', '1', 'aovwn_179283', '青岛天汇玛莎拉蒂专卖资源表', '1', null, '山东', null, '2016-12-20 10:33:00', '/index.php?c=com&m=zyInfo&uid=aovwn_179283', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('59', '1', 'uthwg_231095', '北京耀阳盛世资源表', '1', null, '北京', null, '2016-12-20 10:33:00', '/index.php?c=com&m=zyInfo&uid=uthwg_231095', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('60', '1', 'qfgqy_46632', '深圳市前海拓新资源表', '1', null, '广东', null, '2016-12-20 10:33:00', '/index.php?c=com&m=zyInfo&uid=qfgqy_46632', '0', '2016-12-20 10:49:32');
INSERT INTO `car_resource` VALUES ('61', '1', 'tldqn_2799', '张彬个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=tldqn_2799', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('62', '1', 'biqfy_70915', '赵留建个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=biqfy_70915', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('63', '1', 'wsasi_197953', '张鹏举个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=wsasi_197953', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('64', '1', 'jejjc_91650', '王章峰个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=jejjc_91650', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('65', '1', 'swful_166618', '沈利冉个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=swful_166618', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('66', '1', 'gvtad_175734', '戈福兵个人资源表', '1', null, '北京', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=gvtad_175734', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('67', '1', 'bndee_141915', '张彩云个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=bndee_141915', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('68', '1', 'rivek_29352', '朱慧仅个人资源表', '1', null, '北京', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=rivek_29352', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('69', '1', 'lvmmq_110065', '郭群超个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=lvmmq_110065', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('70', '1', 'zaanv_5122', '杨柳个人资源表', '1', null, '辽宁', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=zaanv_5122', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('71', '1', 'jkhxf_59943', '孙兆梦个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=jkhxf_59943', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('72', '1', 'zogbf_98125', '王叶个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=zogbf_98125', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('73', '1', 'dkkxt_25770', '刘亚丽个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=dkkxt_25770', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('74', '1', 'ixhhs_180799', '张永飞个人资源表', '1', null, '河南', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=ixhhs_180799', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('75', '1', 'ncndc_40887', '刘德民个人资源表', '1', null, '天津', null, '2016-12-20 10:24:00', '/index.php?c=com&m=zyInfo&uid=ncndc_40887', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('76', '1', 'plshv_4940', '刘敏个人资源表', '1', null, '北京', null, '2016-12-20 10:23:00', '/index.php?c=com&m=zyInfo&uid=plshv_4940', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('77', '1', 'gsbmn_2702', '白锦宏个人资源表', '1', null, '天津', null, '2016-12-20 10:23:00', '/index.php?c=com&m=zyInfo&uid=gsbmn_2702', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('78', '1', 'jfmds_67924', '王爽个人资源表', '1', null, '北京', null, '2016-12-20 10:23:00', '/index.php?c=com&m=zyInfo&uid=jfmds_67924', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('79', '1', 'mxajo_211122', '邓程程个人资源表', '1', null, '安徽', null, '2016-12-20 10:23:00', '/index.php?c=com&m=zyInfo&uid=mxajo_211122', '0', '2016-12-20 10:49:36');
INSERT INTO `car_resource` VALUES ('80', '1', 'mkvcm_163187', '李天旬个人资源表', '1', null, '河南', null, '2016-12-20 10:23:00', '/index.php?c=com&m=zyInfo&uid=mkvcm_163187', '0', '2016-12-20 10:49:36');
