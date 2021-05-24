/*
Navicat MySQL Data Transfer

Source Server         : 211.155.92.176-toc从库
Source Server Version : 50621
Source Host           : 211.155.92.176:3306
Source Database       : obdvin_log

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2014-12-22 10:45:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for accident_message
-- ----------------------------
DROP TABLE IF EXISTS `accident_message`;
CREATE TABLE `accident_message` (
  `message_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '异常信息id',
  `vin` varchar(30) DEFAULT NULL COMMENT '车架号',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBD设备id',
  `message_type` int(11) DEFAULT NULL COMMENT '异常信息id，0：obd激活；1：电子围栏越界；2：异常移动；3：碰撞；4：故障；',
  `message_level` int(11) DEFAULT NULL COMMENT '异常级别，数值越小级别越高',
  `message` text COMMENT '消息内容',
  `message_value` varchar(255) DEFAULT NULL COMMENT '值',
  `alter_content` varchar(100) DEFAULT NULL COMMENT '提醒内容',
  `title` varchar(20) DEFAULT NULL COMMENT '标题',
  `longitude` decimal(20,8) DEFAULT NULL COMMENT '经度',
  `latitude` decimal(20,8) DEFAULT NULL COMMENT '纬度',
  `send_status` smallint(6) DEFAULT '0' COMMENT '是否发送，0为发送，1已发送',
  `send_time` datetime DEFAULT NULL COMMENT '发送时间', 
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '服务器端创建时间',
  `message_from` varchar(20) DEFAULT '' COMMENT '用户设置的电子围栏的ID',
  `message_name` varchar(30) DEFAULT NULL COMMENT '消息的标识',
  `address` varchar(100) DEFAULT '',
  PRIMARY KEY (`message_id`),
  KEY `kidx` (`obd_id`,`create_time`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1140505 DEFAULT CHARSET=utf8 COMMENT='车辆异常信息表';

-- ----------------------------
-- Table structure for account_grade_func_stat
-- ----------------------------
DROP TABLE IF EXISTS `account_grade_func_stat`;
CREATE TABLE `account_grade_func_stat` (
  `account_id` bigint(20) DEFAULT NULL COMMENT 'è´¦æˆ·id',
  `item_key` int(11) DEFAULT NULL COMMENT 'é¡¹ç›®é”®',
  `item_count` int(11) DEFAULT NULL COMMENT 'è¡Œä¸ºæ¬¡æ•°',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'æ›´æ–°æ—¥æœŸ',
  KEY `index_1` (`account_id`,`item_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='ä¸ªäººæˆå°±åŠŸèƒ½ä½¿ç”¨ç»Ÿè®¡è¡¨';

-- ----------------------------
-- Table structure for account_grade_item
-- ----------------------------
DROP TABLE IF EXISTS `account_grade_item`;
CREATE TABLE `account_grade_item` (
  `item_key` int(11) DEFAULT NULL COMMENT 'é¡¹ç›®é”®',
  `item_name` varchar(50) DEFAULT NULL COMMENT 'é¡¹ç›®åç§°',
  `item_type` smallint(6) DEFAULT NULL COMMENT 'é¡¹ç›®ç±»åž‹ï¼š0ï¼Œç”¨æˆ·ä¿¡æ¯ï¼Œ2ï¼ŒåŠŸèƒ½ä½¿ç”¨ï¼›3ï¼Œä»»åŠ¡',
  `item_score` int(11) DEFAULT NULL COMMENT 'åˆ†å€¼'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='ä¸ªäººæˆå°±åŠ åˆ†é¡¹é…ç½®è¡¨';

-- ----------------------------
-- Table structure for account_grade_status
-- ----------------------------
DROP TABLE IF EXISTS `account_grade_status`;
CREATE TABLE `account_grade_status` (
  `account_id` bigint(20) NOT NULL COMMENT 'è´¦æˆ·id',
  `account_score` int(11) DEFAULT NULL COMMENT 'ç”¨æˆ·ç§¯åˆ†',
  `account_grade` smallint(6) DEFAULT '1' COMMENT 'ç”¨æˆ·ç­‰çº§',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'æœ€åŽè®¡ç®—æ—¥æœŸ',
  PRIMARY KEY (`account_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='ä¸ªäººæˆå°±è¡¨';

-- ----------------------------
-- Table structure for account_grade_task_ext_info
-- ----------------------------
DROP TABLE IF EXISTS `account_grade_task_ext_info`;
CREATE TABLE `account_grade_task_ext_info` (
  `item_key` int(11) DEFAULT NULL COMMENT 'é¡¹ç›®é”®',
  `item_cycle` varchar(100) DEFAULT NULL COMMENT 'é¡¹ç›®å‘¨æœŸ',
  `finish_condition` varchar(200) DEFAULT NULL COMMENT 'ä»»åŠ¡å®Œæˆæ¡ä»¶'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='ä¸ªäººæˆå°±ä»»åŠ¡æ‰©å±•è¡¨';

-- ----------------------------
-- Table structure for account_grade_task_stat
-- ----------------------------
DROP TABLE IF EXISTS `account_grade_task_stat`;
CREATE TABLE `account_grade_task_stat` (
  `account_id` bigint(20) DEFAULT NULL COMMENT 'è´¦æˆ·id',
  `item_key` int(11) DEFAULT NULL COMMENT 'é¡¹ç›®é”®',
  `item_count` int(11) DEFAULT NULL COMMENT 'è¡Œä¸ºæ¬¡æ•°',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'è¡Œä¸ºæ—¥æœŸ'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='ä¸ªäººæˆå°±è¿è¥ä»»åŠ¡ç»Ÿè®¡è¡¨';

-- ----------------------------
-- Table structure for account_profile
-- ----------------------------
DROP TABLE IF EXISTS `account_profile`;
CREATE TABLE `account_profile` (
  `account_id` bigint(20) DEFAULT NULL COMMENT 'è´¦æˆ·id',
  `item_key` int(11) DEFAULT NULL COMMENT 'é¡¹ç›®é”®',
  `item_content` varchar(100) DEFAULT NULL COMMENT 'é¡¹ç›®å€¼',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'å®Œæˆæ—¶é—´',
  `update_time` datetime DEFAULT NULL COMMENT 'æ›´æ–°æ—¶é—´',
  KEY `index_1` (`account_id`,`item_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='ç”¨æˆ·ä¿¡æ¯è¡¨';

-- ----------------------------
-- Table structure for analysis_cool_oil
-- ----------------------------
DROP TABLE IF EXISTS `analysis_cool_oil`;
CREATE TABLE `analysis_cool_oil` (
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `type` varchar(10) DEFAULT NULL COMMENT '统计类型',
  `item` int(10) DEFAULT NULL COMMENT '统计维度',
  `item_value` double(10,0) NOT NULL DEFAULT '0' COMMENT '统计值',
  `extr_flag` varchar(10) DEFAULT NULL COMMENT '是否是最大值，最小值（0为最小温度，1为最大温度）'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for collidefire
-- ----------------------------
DROP TABLE IF EXISTS `collidefire`;
CREATE TABLE `collidefire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(30) DEFAULT NULL,
  `stoptime` datetime DEFAULT NULL,
  `collide` datetime DEFAULT NULL,
  `fire` datetime DEFAULT NULL,
  `diff` int(8) DEFAULT NULL,
  `gps` datetime DEFAULT NULL,
  `gps_diff` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `didjxc88233b` (`obd_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=357349 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for collidefire8
-- ----------------------------
DROP TABLE IF EXISTS `collidefire8`;
CREATE TABLE `collidefire8` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(30) DEFAULT NULL,
  `stoptime` datetime DEFAULT NULL,
  `collide` datetime DEFAULT NULL,
  `fire` datetime DEFAULT NULL,
  `diff` int(8) DEFAULT NULL,
  `gps` datetime DEFAULT NULL,
  `gps_diff` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dssd34ewvr4cvfsvfczx` (`obd_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=110070 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for command_from_app
-- ----------------------------
DROP TABLE IF EXISTS `command_from_app`;
CREATE TABLE `command_from_app` (
  `command_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBD设备号',
  `vin` varchar(30) DEFAULT NULL COMMENT '车架号',
  `data_type` smallint(6) DEFAULT '0' COMMENT '数据类型',
  `cmd_request_name` varchar(50) DEFAULT NULL COMMENT '请求类型',
  `cmd_name` varchar(50) DEFAULT NULL COMMENT '请求名称',
  `cmd_status` smallint(6) DEFAULT NULL COMMENT '请求状态',
  `create_time` datetime DEFAULT NULL COMMENT '数据创建时间',
  `operation_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '操作完成时间',
  `imsi` varchar(50) DEFAULT NULL COMMENT 'IMSI',
  `mobile` varchar(20) DEFAULT NULL COMMENT 'obd中imsi号码',
  PRIMARY KEY (`command_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14532 DEFAULT CHARSET=utf8 COMMENT='APP数据请求记录';

-- ----------------------------
-- Table structure for device_latest_e2
-- ----------------------------
DROP TABLE IF EXISTS `device_latest_e2`;
CREATE TABLE `device_latest_e2` (
  `id` bigint(20) DEFAULT NULL,
  `vin` varchar(100) DEFAULT NULL,
  `obd_id` varchar(50) DEFAULT NULL,
  `function_id` varchar(4) DEFAULT NULL,
  `message_id` varchar(4) DEFAULT NULL,
  `message_content` text,
  `longitude` decimal(18,6) DEFAULT NULL,
  `latitude` decimal(18,6) DEFAULT NULL,
  `speed` int(11) DEFAULT NULL,
  `engine_speed` int(11) DEFAULT NULL,
  `gps_stat` varchar(20) DEFAULT NULL,
  `client_time` datetime DEFAULT NULL,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `analytical_result` varchar(30) DEFAULT NULL COMMENT '内容解析(碰撞..)',
  UNIQUE KEY `idx_latest_e2_obdId` (`obd_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for device_status_log
-- ----------------------------
DROP TABLE IF EXISTS `device_status_log`;
CREATE TABLE `device_status_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vin` varchar(30) NOT NULL COMMENT 'è½¦æž¶å·',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBDè®¾å¤‡id',
  `function_id` varchar(4) DEFAULT NULL COMMENT 'åŠŸèƒ½id(fid)ï¼Œè§¦å‘å™¨',
  `message_id` varchar(4) DEFAULT NULL COMMENT 'æ¶ˆæ¯id',
  `message_content` text COMMENT 'çŠ¶æ€æˆ–äº‹ä»¶ä¿¡æ¯ï¼šé”®å€¼å¯¹ï¼škey1=>value,key2=>value,...ã€‚é€—å·åˆ†å‰²çš„é”®å€¼å¯¹',
  `longitude` decimal(18,6) DEFAULT NULL COMMENT 'ç»åº¦',
  `latitude` decimal(18,6) DEFAULT NULL COMMENT 'çº¬åº¦',
  `speed` int(11) DEFAULT NULL COMMENT 'é€Ÿåº¦',
  `engine_speed` int(11) DEFAULT NULL COMMENT 'è½¬é€Ÿ',
  `gps_stat` varchar(20) DEFAULT NULL COMMENT 'GPSçŠ¶æ€',
  `client_time` datetime DEFAULT NULL COMMENT 'å®¢æˆ·ç«¯æ—¶é—´',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'æœåŠ¡å™¨ç«¯åˆ›å»ºæ—¶é—´',
  `analytical_result` varchar(30) DEFAULT NULL COMMENT '内容解析(碰撞..)',
  PRIMARY KEY (`id`),
  KEY `device_status_obd_msg_idx01` (`obd_id`,`message_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30454067 DEFAULT CHARSET=utf8 COMMENT='è½¦å†µåŠOBDæ—¥å¿—';

-- ----------------------------
-- Table structure for dtc_get
-- ----------------------------
DROP TABLE IF EXISTS `dtc_get`;
CREATE TABLE `dtc_get` (
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBDè®¾å¤‡id',
  `message_content` text COMMENT 'çŠ¶æ€æˆ–äº‹ä»¶ä¿¡æ¯ï¼šé”®å€¼å¯¹ï¼škey1=>value,key2=>value,...ã€‚é€—å·åˆ†å‰²çš„é”®å€¼å¯¹',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'æœåŠ¡å™¨ç«¯åˆ›å»ºæ—¶é—´',
  `d1` varchar(8) DEFAULT NULL,
  `d2` varchar(8) DEFAULT NULL,
  `d3` varchar(8) DEFAULT NULL,
  `d4` varchar(8) DEFAULT NULL,
  `d5` varchar(8) DEFAULT NULL,
  `d6` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for gsensor_log
-- ----------------------------
DROP TABLE IF EXISTS `gsensor_log`;
CREATE TABLE `gsensor_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(50) DEFAULT NULL,
  `message_content` text COMMENT 'gsensor消息',
  `result` varchar(50) DEFAULT NULL COMMENT '碰撞力度',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `client_time` datetime DEFAULT NULL,
  `remark` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1246726 DEFAULT CHARSET=utf8 COMMENT='2b消息（碰撞消息日志表）';

-- ----------------------------
-- Table structure for locus
-- ----------------------------
DROP TABLE IF EXISTS `locus`;
CREATE TABLE `locus` (
  `tid` int(11) NOT NULL,
  `obd_id` varchar(50) NOT NULL,
  `points` mediumtext,
  `mileage` float DEFAULT '0',
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `up_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`tid`),
  UNIQUE KEY `kidx` (`obd_id`,`start_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_all
-- ----------------------------
DROP TABLE IF EXISTS `locus_all`;
CREATE TABLE `locus_all` (
  `tid` int(11) NOT NULL,
  `obd_id` varchar(50) NOT NULL,
  `points` mediumtext,
  `mileage` float DEFAULT '0',
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `up_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`tid`),
  UNIQUE KEY `kidx` (`obd_id`,`start_time`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_analyse_stop
-- ----------------------------
DROP TABLE IF EXISTS `locus_analyse_stop`;
CREATE TABLE `locus_analyse_stop` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `tid` int(11) NOT NULL COMMENT '行程编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `longitude` varchar(30) NOT NULL COMMENT '经度',
  `latitude` varchar(30) NOT NULL DEFAULT '' COMMENT '纬度',
  `stop_time` datetime NOT NULL COMMENT '开始停留时间',
  `stop_len` int(11) NOT NULL COMMENT '停留时长',
  `poi_name` varchar(80) NOT NULL COMMENT 'poi名称',
  `poi_address` varchar(200) NOT NULL COMMENT '地址',
  `cont` text COMMENT '查询',
  `flag` int(10) DEFAULT '0' COMMENT '重复停留标记',
  `weekend_flag` int(10) DEFAULT '0' COMMENT '周末停留标记',
  `radius` int(10) DEFAULT '0' COMMENT '活动半径',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`,`stop_time`) USING HASH
) ENGINE=MyISAM AUTO_INCREMENT=2966616 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_analyse_travel
-- ----------------------------
DROP TABLE IF EXISTS `locus_analyse_travel`;
CREATE TABLE `locus_analyse_travel` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `type` varchar(50) NOT NULL,
  `start_point` varchar(100) NOT NULL COMMENT '起点经纬度',
  `start_stop_id` int(11) NOT NULL,
  `end_point` varchar(100) NOT NULL DEFAULT '' COMMENT '终点经纬度',
  `end_stop_id` int(11) NOT NULL,
  `travel_content` mediumtext COMMENT '里程',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`,`type`)
) ENGINE=MyISAM AUTO_INCREMENT=8061 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_analyse_travel_road
-- ----------------------------
DROP TABLE IF EXISTS `locus_analyse_travel_road`;
CREATE TABLE `locus_analyse_travel_road` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `tid` int(11) NOT NULL COMMENT '行程编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `type` varchar(50) NOT NULL COMMENT '类型(h2c家-公司, c2h公司-家)',
  `road` mediumtext NOT NULL COMMENT '路径详细描述',
  `troad` text NOT NULL COMMENT '路径简略',
  `mileage` text,
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tidx` (`obd_id`,`tid`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=633784 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_bycar
-- ----------------------------
DROP TABLE IF EXISTS `locus_bycar`;
CREATE TABLE `locus_bycar` (
  `bid` int(11) NOT NULL AUTO_INCREMENT COMMENT '借车报告编号',
  `user_id` int(11) NOT NULL COMMENT '用户号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd编号',
  `byname` varchar(200) DEFAULT NULL COMMENT '借车人名字',
  `start_time` datetime DEFAULT NULL COMMENT '开始时间',
  `end_time` datetime DEFAULT NULL COMMENT '结束时间',
  `bytimelen` int(10) DEFAULT NULL COMMENT '借车时长',
  `score` int(10) NOT NULL COMMENT '评分',
  `violation_count` int(10) DEFAULT '0' COMMENT '违章次数',
  `fault_count` int(10) DEFAULT '0' COMMENT '故障次数',
  `mileage` int(10) DEFAULT NULL COMMENT '里程数',
  `tag` enum('1','0') DEFAULT '1' COMMENT '删除标记',
  `tagby` enum('1','0') DEFAULT '1' COMMENT '0出借中，1已借完',
  PRIMARY KEY (`bid`)
) ENGINE=MyISAM AUTO_INCREMENT=4624 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_bycar_detail
-- ----------------------------
DROP TABLE IF EXISTS `locus_bycar_detail`;
CREATE TABLE `locus_bycar_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '借车明细编号',
  `bid` int(11) NOT NULL COMMENT '借车详情编号',
  `sid` int(11) NOT NULL COMMENT '行程编号',
  `travel_date` datetime NOT NULL COMMENT '行程日期',
  `violation_count` int(10) DEFAULT '0' COMMENT '违章次数',
  `fault_count` int(10) DEFAULT '0' COMMENT '故障次数',
  `mileage` int(10) DEFAULT '0' COMMENT '里程',
  `avgspeed` float DEFAULT '0' COMMENT '平均车速',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6739 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_car_score
-- ----------------------------
DROP TABLE IF EXISTS `locus_car_score`;
CREATE TABLE `locus_car_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `score_date` datetime NOT NULL COMMENT '创建时间',
  `score` int(10) NOT NULL COMMENT '得分',
  `level` int(10) NOT NULL COMMENT '等级',
  `cid` int(10) NOT NULL DEFAULT '5' COMMENT '评语编号',
  `shid` int(10) NOT NULL DEFAULT '9' COMMENT '分享话术编号',
  `description` text COMMENT '描述',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`,`score_date`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=609652 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_car_score_detail
-- ----------------------------
DROP TABLE IF EXISTS `locus_car_score_detail`;
CREATE TABLE `locus_car_score_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL COMMENT '评分编号',
  `type` enum('COMPLEX','PID','DTC') NOT NULL COMMENT '类型',
  `class` varchar(20) NOT NULL COMMENT '分类',
  `extent` enum('严重','中等','一般','轻微') DEFAULT NULL COMMENT '严重程度',
  `code` varchar(20) NOT NULL COMMENT '故障码',
  `value` float(255,0) DEFAULT NULL COMMENT '值',
  `descrption` varchar(250) DEFAULT NULL COMMENT '描述',
  `subscore` int(10) DEFAULT NULL COMMENT '得分',
  `suggest` varchar(250) DEFAULT NULL COMMENT '建议',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `评分编号` (`sid`)
) ENGINE=MyISAM AUTO_INCREMENT=366672 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_comment
-- ----------------------------
DROP TABLE IF EXISTS `locus_comment`;
CREATE TABLE `locus_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `type` int(10) NOT NULL COMMENT '类型11-16驾驶评语，21-26车况评语',
  `Comment` text NOT NULL COMMENT '评语',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=110 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_dtc_comment
-- ----------------------------
DROP TABLE IF EXISTS `locus_dtc_comment`;
CREATE TABLE `locus_dtc_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
  `code` varchar(20) NOT NULL,
  `type` varchar(100) NOT NULL COMMENT '类型',
  `level` varchar(30) NOT NULL COMMENT '等级',
  `description` varchar(250) NOT NULL COMMENT '描述',
  `aftermath` varchar(250) NOT NULL COMMENT '不处理的后果',
  `remind` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1091 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_dtc_comment_copy
-- ----------------------------
DROP TABLE IF EXISTS `locus_dtc_comment_copy`;
CREATE TABLE `locus_dtc_comment_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
  `code` varchar(20) NOT NULL,
  `type` varchar(100) NOT NULL COMMENT '类型',
  `level` varchar(30) NOT NULL COMMENT '等级',
  `description` varchar(250) NOT NULL COMMENT '描述',
  `aftermath` varchar(250) NOT NULL COMMENT '不处理的后果',
  `remind` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1025 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_exchange
-- ----------------------------
DROP TABLE IF EXISTS `locus_exchange`;
CREATE TABLE `locus_exchange` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  `content` mediumtext NOT NULL,
  `create_time` datetime NOT NULL COMMENT '生成时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_for_app
-- ----------------------------
DROP TABLE IF EXISTS `locus_for_app`;
CREATE TABLE `locus_for_app` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `tid` int(11) NOT NULL COMMENT '行程号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `longitude` varchar(50) NOT NULL COMMENT '经度',
  `latitude` varchar(50) NOT NULL COMMENT '纬度',
  `filter_flag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '50点筛点标志,1为选中的点',
  `stop_flag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '停留点标志',
  `speed_level` enum('5','4','3','2','1') DEFAULT '1' COMMENT '速度等级1-5',
  `poi_name` varchar(200) DEFAULT NULL COMMENT '停留点名称',
  `poi_address` varchar(250) DEFAULT NULL COMMENT '停留点地址',
  `stop_time_len` int(10) DEFAULT NULL COMMENT '停留时长(秒)',
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `obdct` (`tid`,`create_time`) USING HASH,
  KEY `obdidx` (`obd_id`,`create_time`)
) ENGINE=MyISAM AUTO_INCREMENT=253243707 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_gps_log
-- ----------------------------
DROP TABLE IF EXISTS `locus_gps_log`;
CREATE TABLE `locus_gps_log` (
  `id` int(11) NOT NULL COMMENT '编号',
  `vin` varchar(30) NOT NULL COMMENT 'vin码',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBD编号',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT NULL COMMENT '纬度',
  `speed` varchar(10) DEFAULT NULL COMMENT '速度',
  `engine_speed` varchar(10) DEFAULT NULL COMMENT '引擎转速',
  `gps_stat` varchar(20) DEFAULT NULL COMMENT 'GPS状态',
  `client_time` datetime DEFAULT NULL COMMENT 'gps时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '服务器时间',
  `coolant` varchar(10) DEFAULT NULL COMMENT '水温',
  `intakeMAP` varchar(10) DEFAULT NULL COMMENT '进气压力',
  `intakeAir` varchar(10) DEFAULT NULL COMMENT '进气温度',
  `absolute_throttle` varchar(10) DEFAULT NULL COMMENT '节气门开度',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`id`) USING BTREE,
  KEY `qidx` (`obd_id`,`gps_stat`,`create_time`) USING BTREE,
  KEY `qcdx` (`obd_id`,`gps_stat`,`client_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='gps记录';

-- ----------------------------
-- Table structure for locus_outsend
-- ----------------------------
DROP TABLE IF EXISTS `locus_outsend`;
CREATE TABLE `locus_outsend` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `user` varchar(100) NOT NULL,
  `passwd` varchar(100) NOT NULL,
  `name` varchar(255) DEFAULT NULL COMMENT '中文名称',
  `filter_obd` longtext,
  `filter_field` longtext COMMENT '禁止项',
  `filter_sql` longtext,
  `downlog` longtext,
  `token` varchar(100) DEFAULT NULL COMMENT '令牌',
  `last_time` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_pid_comment
-- ----------------------------
DROP TABLE IF EXISTS `locus_pid_comment`;
CREATE TABLE `locus_pid_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
  `code` varchar(20) NOT NULL,
  `type` varchar(100) NOT NULL COMMENT '类型',
  `level` varchar(30) NOT NULL COMMENT '等级',
  `description` varchar(250) NOT NULL COMMENT '描述',
  `aftermath` varchar(250) NOT NULL COMMENT '不处理的后果',
  `remind` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=706 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_score
-- ----------------------------
DROP TABLE IF EXISTS `locus_score`;
CREATE TABLE `locus_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `score_date` datetime NOT NULL COMMENT '评分时间',
  `score` int(10) NOT NULL COMMENT '评分0-100',
  `level` int(10) DEFAULT NULL COMMENT '等级1-5',
  `sort` int(10) DEFAULT NULL COMMENT '排名',
  `avg_score` int(10) DEFAULT NULL COMMENT '历史平均评分',
  `cid` int(11) DEFAULT '11' COMMENT '评语id',
  `shid` int(10) DEFAULT '4' COMMENT '分享话术编号',
  `locus_count` int(10) DEFAULT NULL COMMENT '当日行程数',
  `locus_alltime` int(10) DEFAULT NULL COMMENT '当日行程总时长',
  `locus_maxtime` int(10) DEFAULT NULL COMMENT '当日单次行程最大时长',
  `mileage` float DEFAULT NULL COMMENT '里程数',
  `maxspeed` int(10) DEFAULT NULL COMMENT '1天内最高速度',
  `avgspeed` float DEFAULT NULL COMMENT '平均速度',
  `highspeed_count` int(10) DEFAULT '0' COMMENT '超速次数',
  `speed_up` int(10) DEFAULT NULL COMMENT '急加速',
  `speed_down` int(10) DEFAULT NULL COMMENT '急减速',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`,`obd_id`,`score_date`),
  UNIQUE KEY `kidx` (`obd_id`,`score_date`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=374527 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_score_rank
-- ----------------------------
DROP TABLE IF EXISTS `locus_score_rank`;
CREATE TABLE `locus_score_rank` (
  `percentage` int(11) NOT NULL,
  `score` int(11) DEFAULT NULL,
  PRIMARY KEY (`percentage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_status_log
-- ----------------------------
DROP TABLE IF EXISTS `locus_status_log`;
CREATE TABLE `locus_status_log` (
  `id` int(11) NOT NULL,
  `vin` varchar(30) NOT NULL COMMENT '车架号',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBD编号',
  `function_id` varchar(4) DEFAULT NULL COMMENT '功能id',
  `message_id` varchar(4) DEFAULT NULL COMMENT '消息id',
  `message_content` text COMMENT '消息内容',
  `longitude` decimal(18,6) DEFAULT NULL COMMENT '精度',
  `latitude` decimal(18,6) DEFAULT NULL COMMENT '纬度',
  `speed` int(11) DEFAULT NULL COMMENT '速度',
  `engine_speed` int(11) DEFAULT NULL COMMENT '引擎',
  `gps_stat` varchar(20) DEFAULT NULL COMMENT 'GPS状态',
  `client_time` datetime DEFAULT NULL COMMENT 'obd时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '服务器时间',
  `analytical_result` varchar(30) DEFAULT NULL COMMENT '内容解析(碰撞..)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`id`) USING BTREE,
  KEY `kqdx` (`obd_id`,`message_id`,`create_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='最近状态表';

-- ----------------------------
-- Table structure for locus_travel
-- ----------------------------
DROP TABLE IF EXISTS `locus_travel`;
CREATE TABLE `locus_travel` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '行程编号',
  `vin` varchar(30) DEFAULT NULL COMMENT '车架号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `start_id` int(11) NOT NULL COMMENT '开始序号',
  `end_id` int(11) NOT NULL COMMENT '结束序号',
  `start_time` datetime DEFAULT NULL COMMENT '开始时间',
  `end_time` datetime DEFAULT NULL COMMENT '结束时间',
  `score` int(10) DEFAULT '0' COMMENT '单次行程评分',
  `cid` int(11) DEFAULT '11' COMMENT '评语编号',
  `shid` int(11) DEFAULT '4' COMMENT '分享话术编号',
  `mileage` float DEFAULT NULL COMMENT '里程',
  `distance` float DEFAULT '0' COMMENT 'obd上传的里程',
  `fuel` float DEFAULT '0' COMMENT '油耗',
  `fuel_id` varchar(600) DEFAULT '0' COMMENT '状态编号',
  `travel_ratio` float DEFAULT '1' COMMENT '跨天占比',
  `start_point` varchar(100) DEFAULT NULL COMMENT '开始点',
  `end_point` varchar(100) DEFAULT NULL COMMENT '结束点',
  `start_name` varchar(200) DEFAULT NULL COMMENT '开始点名称',
  `end_name` varchar(200) DEFAULT NULL COMMENT '结束点名称',
  `maxspeed` int(10) DEFAULT NULL COMMENT '单次行程最高速',
  `avgspeed` float DEFAULT NULL COMMENT '平均速度',
  `avgs_count` int(10) DEFAULT NULL COMMENT '平均个数',
  `avgengine` int(10) DEFAULT NULL COMMENT '平均转数',
  `lazy_count` int(10) DEFAULT NULL COMMENT '怠速次数',
  `highspeed_count` int(10) DEFAULT '0' COMMENT '超速次数',
  `speed_up` int(10) DEFAULT '0' COMMENT '急加速次数',
  `speed_down` int(10) DEFAULT '0' COMMENT '急减速次数',
  `flag` int(10) DEFAULT '0' COMMENT '数据处理标致',
  `flag2` int(10) DEFAULT '0' COMMENT '停留处理标志',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tkidx` (`obd_id`,`start_id`) USING BTREE,
  KEY `tsidx` (`obd_id`,`start_time`) USING BTREE,
  KEY `tcidx` (`create_time`,`obd_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2337815 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_travel_copy
-- ----------------------------
DROP TABLE IF EXISTS `locus_travel_copy`;
CREATE TABLE `locus_travel_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '行程编号',
  `vin` varchar(30) DEFAULT NULL COMMENT '车架号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `start_id` int(11) NOT NULL COMMENT '开始序号',
  `end_id` int(11) NOT NULL COMMENT '结束序号',
  `start_time` datetime DEFAULT NULL COMMENT '开始时间',
  `end_time` datetime DEFAULT NULL COMMENT '结束时间',
  `score` int(10) DEFAULT '0' COMMENT '单次行程评分',
  `cid` int(11) DEFAULT '11' COMMENT '评语编号',
  `shid` int(11) DEFAULT '4' COMMENT '分享话术编号',
  `mileage` float DEFAULT NULL COMMENT '里程',
  `distance` float DEFAULT '0' COMMENT 'obd上传的里程',
  `fuel` float DEFAULT '0' COMMENT '油耗',
  `fuel_id` varchar(120) DEFAULT '0' COMMENT '状态编号',
  `travel_ratio` float DEFAULT '1' COMMENT '跨天占比',
  `start_point` varchar(100) DEFAULT NULL COMMENT '开始点',
  `end_point` varchar(100) DEFAULT NULL COMMENT '结束点',
  `start_name` varchar(200) DEFAULT NULL COMMENT '开始点名称',
  `end_name` varchar(200) DEFAULT NULL COMMENT '结束点名称',
  `maxspeed` int(10) DEFAULT NULL COMMENT '单次行程最高速',
  `avgspeed` float DEFAULT NULL COMMENT '平均速度',
  `avgs_count` int(10) DEFAULT NULL COMMENT '平均个数',
  `avgengine` int(10) DEFAULT NULL COMMENT '平均转数',
  `lazy_count` int(10) DEFAULT NULL COMMENT '怠速次数',
  `highspeed_count` int(10) DEFAULT '0' COMMENT '超速次数',
  `speed_up` int(10) DEFAULT '0' COMMENT '急加速次数',
  `speed_down` int(10) DEFAULT '0' COMMENT '急减速次数',
  `flag` int(10) DEFAULT '0' COMMENT '数据处理标致',
  `flag2` int(10) DEFAULT '0' COMMENT '停留处理标志',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tkidx` (`obd_id`,`start_id`) USING BTREE,
  KEY `tsidx` (`obd_id`,`start_time`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1159245 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_travel_detail
-- ----------------------------
DROP TABLE IF EXISTS `locus_travel_detail`;
CREATE TABLE `locus_travel_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
  `tid` int(11) NOT NULL COMMENT '行程编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `type` varchar(50) NOT NULL COMMENT '类别',
  `value` int(11) NOT NULL COMMENT '数值',
  `create_time` datetime NOT NULL COMMENT '发生时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`tid`,`obd_id`,`type`) USING HASH
) ENGINE=MyISAM AUTO_INCREMENT=2411998 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_vin_parse
-- ----------------------------
DROP TABLE IF EXISTS `locus_vin_parse`;
CREATE TABLE `locus_vin_parse` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd编号',
  `vin` varchar(50) DEFAULT NULL COMMENT '车架号',
  `type` int(10) DEFAULT '1' COMMENT '1 obd采集的vin码，0 用户输入的vin码',
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `md` float DEFAULT '1' COMMENT '汽油密度',
  `pl` float DEFAULT '1.8' COMMENT '排量',
  `xs` float DEFAULT '1' COMMENT '系数',
  `wid` int(11) DEFAULT '1' COMMENT '车型水温区间id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29314 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_vin_parse1
-- ----------------------------
DROP TABLE IF EXISTS `locus_vin_parse1`;
CREATE TABLE `locus_vin_parse1` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd编号',
  `vin` varchar(50) DEFAULT NULL COMMENT '车架号',
  `type` int(10) DEFAULT '1' COMMENT '1 obd采集的vin码，0 用户输入的vin码',
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `md` float DEFAULT '1' COMMENT '汽油密度',
  `pl` float DEFAULT '1.8' COMMENT '排量',
  `xs` float DEFAULT '1' COMMENT '系数',
  `wid` int(11) DEFAULT '1' COMMENT '车型水温区间id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20527 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_vin_parse_repair
-- ----------------------------
DROP TABLE IF EXISTS `locus_vin_parse_repair`;
CREATE TABLE `locus_vin_parse_repair` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd编号',
  `vin` varchar(50) DEFAULT NULL COMMENT '车架号',
  `type` int(10) DEFAULT '1' COMMENT '1 obd采集的vin码，0 用户输入的vin码',
  `o_cj` varchar(50) DEFAULT NULL COMMENT '错误的厂家',
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `o_nk` varchar(20) DEFAULT NULL COMMENT '错误的年款',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `o_auto` varchar(10) DEFAULT NULL COMMENT '原来错误的手动,自动',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `o_mc` varchar(50) DEFAULT NULL COMMENT '错误的名称',
  `mc` varchar(50) DEFAULT NULL COMMENT '名称',
  `o_pp` varchar(50) DEFAULT NULL COMMENT '错误的品牌',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `o_cx` varchar(50) DEFAULT NULL COMMENT '错误的车型',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `md` float DEFAULT '1' COMMENT '汽油密度',
  `o_pl` float DEFAULT NULL COMMENT '原来错误的排量',
  `pl` float DEFAULT '1.8' COMMENT '排量',
  `xs` float DEFAULT '1' COMMENT '系数',
  `wid` int(11) DEFAULT '1' COMMENT '车型水温区间id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24430 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for locus_water_comment
-- ----------------------------
DROP TABLE IF EXISTS `locus_water_comment`;
CREATE TABLE `locus_water_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `pl` float DEFAULT NULL COMMENT '排量',
  `low` int(10) DEFAULT '0' COMMENT '统计值',
  `high` int(8) DEFAULT NULL,
  `obdcount` int(8) DEFAULT NULL,
  `daycount` int(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_water_1` (`cj`,`nk`,`auto`,`pp`,`cx`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for log_spend
-- ----------------------------
DROP TABLE IF EXISTS `log_spend`;
CREATE TABLE `log_spend` (
  `id` int(11) NOT NULL,
  `oil_name` varchar(100) DEFAULT NULL,
  `wash` varchar(10) DEFAULT NULL,
  `care` varchar(10) DEFAULT NULL,
  `stoptime` datetime(6) DEFAULT NULL,
  `wash27` int(8) DEFAULT '0',
  `stop27` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for log_stop
-- ----------------------------
DROP TABLE IF EXISTS `log_stop`;
CREATE TABLE `log_stop` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `tid` int(11) DEFAULT NULL COMMENT '行程编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT '' COMMENT '纬度',
  `stop_time` datetime DEFAULT NULL COMMENT '开始停留时间',
  `stop_len` int(11) DEFAULT NULL COMMENT '停留时长',
  `poi_name` varchar(80) DEFAULT NULL COMMENT 'poi名称',
  `poi_address` varchar(200) DEFAULT NULL COMMENT '地址',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `oil_name` varchar(100) DEFAULT NULL,
  `wash` varchar(10) DEFAULT NULL,
  `care` varchar(10) DEFAULT NULL,
  `stoptime` datetime(6) DEFAULT NULL,
  `wash27` int(8) DEFAULT NULL,
  `care27` int(11) DEFAULT NULL,
  `bid` int(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `logstopidx1` (`obd_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3084028 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for log_stop1
-- ----------------------------
DROP TABLE IF EXISTS `log_stop1`;
CREATE TABLE `log_stop1` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `tid` int(11) DEFAULT NULL COMMENT '行程编号',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'obd号',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT '' COMMENT '纬度',
  `stop_time` datetime DEFAULT NULL COMMENT '开始停留时间',
  `stop_len` int(11) DEFAULT NULL COMMENT '停留时长',
  `poi_name` varchar(80) DEFAULT NULL COMMENT 'poi名称',
  `poi_address` varchar(200) DEFAULT NULL COMMENT '地址',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `oil_name` varchar(100) DEFAULT NULL,
  `wash` varchar(10) DEFAULT NULL,
  `care` varchar(10) DEFAULT NULL,
  `stoptime` datetime(6) DEFAULT NULL,
  `wash27` int(8) DEFAULT NULL,
  `care27` int(11) DEFAULT NULL,
  `bid` int(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for log_stop2
-- ----------------------------
DROP TABLE IF EXISTS `log_stop2`;
CREATE TABLE `log_stop2` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `tid` int(11) NOT NULL COMMENT '行程编号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT '' COMMENT '纬度',
  `stop_time` datetime DEFAULT NULL COMMENT '开始停留时间',
  `stop_len` int(11) DEFAULT NULL COMMENT '停留时长',
  `poi_name` varchar(80) DEFAULT NULL COMMENT 'poi名称',
  `poi_address` varchar(200) DEFAULT NULL COMMENT '地址',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `oil_name` varchar(100) DEFAULT NULL,
  `wash` varchar(10) DEFAULT NULL,
  `care` varchar(10) DEFAULT NULL,
  `stoptime` datetime(6) DEFAULT NULL,
  `wash27` int(8) DEFAULT NULL,
  `stop27` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6967 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for message_track_log
-- ----------------------------
DROP TABLE IF EXISTS `message_track_log`;
CREATE TABLE `message_track_log` (
  `obd_id` varchar(50) NOT NULL COMMENT 'OBD设备id',
  `start_time` datetime DEFAULT NULL COMMENT '行程开始时间',
  `end_time` datetime DEFAULT NULL COMMENT '行程结束时间',
  `oil_send_status` tinyint(1) DEFAULT '0' COMMENT '油量不足警告提醒，0：未发，1：已发',
  `water_send_status` tinyint(1) DEFAULT '0' COMMENT '水温过高警告提醒，0：未发，1：已发',
  PRIMARY KEY (`obd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='行程消息发送状态表';

-- ----------------------------
-- Table structure for obd_address
-- ----------------------------
DROP TABLE IF EXISTS `obd_address`;
CREATE TABLE `obd_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(50) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `lng` varchar(255) DEFAULT NULL,
  `province` varchar(125) DEFAULT NULL,
  `city` varchar(125) DEFAULT NULL,
  `city_code` varchar(50) DEFAULT NULL,
  `district` varchar(255) DEFAULT NULL,
  `street` varchar(255) DEFAULT NULL,
  `street_number` varchar(255) DEFAULT NULL,
  `weather_date` date DEFAULT NULL,
  `weather_desc` varchar(50) DEFAULT NULL,
  `temperatrue` varchar(50) DEFAULT NULL,
  `wind_direction` varchar(50) DEFAULT NULL,
  `wind_power` varchar(50) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_oa_obd_id` (`obd_id`) USING BTREE,
  KEY `idx_oa_create_time` (`create_time`) USING BTREE,
  KEY `idx_oa_weather_d` (`weather_date`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=510891 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for obd_dtc
-- ----------------------------
DROP TABLE IF EXISTS `obd_dtc`;
CREATE TABLE `obd_dtc` (
  `CODE` char(5) NOT NULL COMMENT '故障码',
  `CTYPE` char(5) NOT NULL COMMENT '车型：all为公有',
  `CTYPE_DESC` varchar(50) DEFAULT NULL COMMENT '车型描述',
  `FAULT_DESC_CN` text COMMENT '故障中文描述',
  `FAULT_DESC_EN` text COMMENT '故障英文描述',
  `FAULT_CATEGORY` varchar(100) DEFAULT NULL COMMENT '故障类型',
  `COMMENT` text COMMENT '备注',
  `SUGGESTION` text,
  `LEVEL` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`CODE`),
  UNIQUE KEY `pk_obd_dtc` (`CODE`,`CTYPE`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='故障码解析';

-- ----------------------------
-- Table structure for obd_last_login
-- ----------------------------
DROP TABLE IF EXISTS `obd_last_login`;
CREATE TABLE `obd_last_login` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(80) DEFAULT NULL,
  `lastdt` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6612 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for obd_latest_address
-- ----------------------------
DROP TABLE IF EXISTS `obd_latest_address`;
CREATE TABLE `obd_latest_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(50) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `lng` varchar(255) DEFAULT NULL,
  `province` varchar(125) DEFAULT NULL,
  `city` varchar(125) DEFAULT NULL,
  `city_code` varchar(50) DEFAULT NULL,
  `district` varchar(255) DEFAULT NULL,
  `street` varchar(255) DEFAULT NULL,
  `street_number` varchar(255) DEFAULT NULL,
  `weather_date` date DEFAULT NULL,
  `weather_desc` varchar(50) DEFAULT NULL,
  `temperatrue` varchar(50) DEFAULT NULL,
  `wind_direction` varchar(50) DEFAULT NULL,
  `wind_power` varchar(50) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_oah_obd_id` (`obd_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12328 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for obd_latest_status
-- ----------------------------
DROP TABLE IF EXISTS `obd_latest_status`;
CREATE TABLE `obd_latest_status` (
  `obd_id` varchar(50) NOT NULL COMMENT 'OBD',
  `vin` varchar(30) NOT NULL COMMENT '车架号',
  `soft_ver` varchar(20) DEFAULT NULL COMMENT 'OBD设备软件版本号',
  `hard_ver` varchar(20) DEFAULT NULL COMMENT 'OBD设备硬件版本号',
  `client_time` datetime DEFAULT NULL COMMENT 'OBD设备时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  `active_time` datetime DEFAULT NULL COMMENT '激活时间',
  `update_time` datetime DEFAULT NULL COMMENT '数据更新时间',
  PRIMARY KEY (`obd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='OBD设备信息表';

-- ----------------------------
-- Table structure for obd_list
-- ----------------------------
DROP TABLE IF EXISTS `obd_list`;
CREATE TABLE `obd_list` (
  `OBD_ID` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for obd_pdsn_depart
-- ----------------------------
DROP TABLE IF EXISTS `obd_pdsn_depart`;
CREATE TABLE `obd_pdsn_depart` (
  `obd_pref` varchar(10) NOT NULL DEFAULT '' COMMENT 'PDSN前缀',
  `cust_code` varchar(10) DEFAULT NULL COMMENT '客户代码',
  `proj_code` varchar(10) DEFAULT NULL COMMENT '项目代码',
  `proj_name` varchar(50) DEFAULT NULL COMMENT '项目名称',
  `proj_desc` text COMMENT '项目说明',
  `comment` text COMMENT '备注',
  PRIMARY KEY (`obd_pref`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='OBD解析表';

-- ----------------------------
-- Table structure for obd_pid
-- ----------------------------
DROP TABLE IF EXISTS `obd_pid`;
CREATE TABLE `obd_pid` (
  `PID` char(2) NOT NULL,
  `CTYPE` char(10) NOT NULL,
  `PARAMETER` int(10) NOT NULL,
  `BYTE_NUM` int(2) DEFAULT NULL,
  `DESC` varchar(50) NOT NULL,
  `BETWEEN` varchar(100) DEFAULT NULL,
  `EXPLAINATION` varchar(100) DEFAULT NULL,
  `UNIT` char(10) DEFAULT NULL,
  `COMMENT` varchar(100) DEFAULT NULL,
  UNIQUE KEY `PK_OBD_PID` (`PID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for pre_locus_for_app
-- ----------------------------
DROP TABLE IF EXISTS `pre_locus_for_app`;
CREATE TABLE `pre_locus_for_app` (
  `id` int(11) NOT NULL COMMENT '编号',
  `tid` int(11) NOT NULL COMMENT '行程号',
  `obd_id` varchar(50) NOT NULL COMMENT 'obd号',
  `longitude` varchar(50) NOT NULL COMMENT '经度',
  `latitude` varchar(50) NOT NULL COMMENT '纬度',
  `filter_flag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '50点筛点标志,1为选中的点',
  `stop_flag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '停留点标志',
  `speed_level` enum('5','4','3','2','1') DEFAULT '1' COMMENT '速度等级1-5',
  `poi_name` varchar(200) DEFAULT NULL COMMENT '停留点名称',
  `poi_address` varchar(250) DEFAULT NULL COMMENT '停留点地址',
  `stop_time_len` int(10) DEFAULT NULL COMMENT '停留时长(秒)',
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `obdct` (`tid`,`create_time`) USING HASH,
  KEY `obdidx` (`obd_id`,`create_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for report_address
-- ----------------------------
DROP TABLE IF EXISTS `report_address`;
CREATE TABLE `report_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(30) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  `card_type` varchar(200) DEFAULT NULL,
  `card_name` varchar(250) DEFAULT NULL,
  `card_address` varchar(250) DEFAULT NULL,
  `longtitude` varchar(30) DEFAULT NULL,
  `latitude` varchar(30) DEFAULT NULL,
  `uptime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`,`sid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for report_address_book
-- ----------------------------
DROP TABLE IF EXISTS `report_address_book`;
CREATE TABLE `report_address_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(50) DEFAULT NULL,
  `stop_id` int(11) DEFAULT NULL,
  `chno` varchar(50) DEFAULT NULL,
  `points` varchar(200) DEFAULT NULL,
  `address_type` int(10) DEFAULT NULL,
  `poi_type` varchar(200) DEFAULT NULL,
  `poi_name` varchar(250) DEFAULT NULL,
  `poi_address` varchar(250) DEFAULT NULL,
  `poi_name_edit` varchar(250) DEFAULT NULL,
  `poi_address_edit` varchar(250) DEFAULT NULL,
  `count` int(10) DEFAULT NULL,
  `hour` int(10) DEFAULT NULL,
  `period` varchar(250) DEFAULT NULL,
  `d6` varchar(50) DEFAULT NULL,
  `d7` varchar(50) DEFAULT NULL,
  `uptime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`obd_id`,`stop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for report_message_detail
-- ----------------------------
DROP TABLE IF EXISTS `report_message_detail`;
CREATE TABLE `report_message_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
  `type` int(5) NOT NULL DEFAULT '1' COMMENT '关联类型(1,路况播报)',
  `aid` int(11) NOT NULL COMMENT '关联id',
  `point` varchar(200) DEFAULT NULL COMMENT '地图中心点',
  `start_point` varchar(200) DEFAULT NULL,
  `end_point` varchar(200) DEFAULT NULL,
  `roadstatus` text NOT NULL COMMENT '道路状况',
  `roaddetail` text COMMENT '路况详细描述',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kidx` (`type`,`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=39687 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for report_province
-- ----------------------------
DROP TABLE IF EXISTS `report_province`;
CREATE TABLE `report_province` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(30) NOT NULL,
  `province` varchar(50) NOT NULL,
  `up_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kindx` (`obd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4602 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for report_robot_session
-- ----------------------------
DROP TABLE IF EXISTS `report_robot_session`;
CREATE TABLE `report_robot_session` (
  `rkey` varchar(50) NOT NULL COMMENT '编号',
  `obd_id` varchar(30) NOT NULL,
  `cont` text NOT NULL COMMENT '内容',
  `uptime` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`rkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for score_rank
-- ----------------------------
DROP TABLE IF EXISTS `score_rank`;
CREATE TABLE `score_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score_up` int(11) DEFAULT NULL,
  `score_down` int(11) DEFAULT NULL,
  `percentage` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for shuser
-- ----------------------------
DROP TABLE IF EXISTS `shuser`;
CREATE TABLE `shuser` (
  `obd_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for stay_log
-- ----------------------------
DROP TABLE IF EXISTS `stay_log`;
CREATE TABLE `stay_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBDID',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT NULL COMMENT '纬度',
  `gps_client_time` datetime DEFAULT NULL,
  `gps_create_time` datetime DEFAULT NULL,
  `gps_stat` varchar(10) DEFAULT NULL,
  `stop_client_time` datetime DEFAULT NULL COMMENT 'gps时间',
  `stop_create_time` datetime DEFAULT NULL COMMENT '入库时间',
  `start_client_time` datetime DEFAULT NULL,
  `start_create_time` datetime DEFAULT NULL,
  `duration` int(8) DEFAULT NULL,
  `oil_name` varchar(80) DEFAULT NULL COMMENT '"Y": near the oil station; else null',
  `collide` int(5) DEFAULT NULL COMMENT '''Y'': has checked this record , else null',
  `class` varchar(8) DEFAULT NULL,
  `stop_now` datetime DEFAULT NULL,
  `start_now` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=266379 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for table_id
-- ----------------------------
DROP TABLE IF EXISTS `table_id`;
CREATE TABLE `table_id` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tablename` varchar(17) NOT NULL DEFAULT '',
  `stat_time` datetime DEFAULT NULL,
  `minid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4071 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for temp_cool_1
-- ----------------------------
DROP TABLE IF EXISTS `temp_cool_1`;
CREATE TABLE `temp_cool_1` (
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `rownum` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tmp_locus_score_rank
-- ----------------------------
DROP TABLE IF EXISTS `tmp_locus_score_rank`;
CREATE TABLE `tmp_locus_score_rank` (
  `score` int(10) NOT NULL COMMENT '评分0-100',
  `amount` bigint(21) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for to_obd_message
-- ----------------------------
DROP TABLE IF EXISTS `to_obd_message`;
CREATE TABLE `to_obd_message` (
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBDè®¾å¤‡id:ä¸åŒOBDæä¾›å•†çš„æœ€å‰ä¸‰ä½éœ€åœ¨æ•´åˆå‰å®šä¹‰',
  `vin` varchar(30) DEFAULT NULL COMMENT 'è½¦æž¶å·',
  `data_type` smallint(6) DEFAULT '0' COMMENT 'æ•°æ®ç±»åž‹',
  `send_data` varchar(50) DEFAULT NULL COMMENT 'æ•°æ®å†…å®¹',
  `cmd_status` smallint(6) DEFAULT NULL COMMENT 'æŒ‡ä»¤æ‰§è¡ŒçŠ¶æ€',
  `mid` varchar(20) DEFAULT NULL COMMENT 'mid',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'åˆ›å»ºæ—¶é—´',
  `send_time` datetime DEFAULT NULL COMMENT 'ä¸‹å‘æ—¶é—´'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='OBDæ¶ˆæ¯ä¸‹å‘è¡¨';

-- ----------------------------
-- Table structure for vehicle_abnormal_speed_stat
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_abnormal_speed_stat`;
CREATE TABLE `vehicle_abnormal_speed_stat` (
  `vin` varchar(30) NOT NULL COMMENT '车架号',
  `acc_on_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '引擎启动时间',
  `acc_off_time` datetime DEFAULT NULL COMMENT '引擎关闭时间',
  `speed_high_count` smallint(6) DEFAULT '0' COMMENT '急加速次数',
  `speed_low_count` smallint(6) DEFAULT '0' COMMENT '急减速次数',
  `over_speed_count` smallint(6) DEFAULT '0' COMMENT '超速次数',
  `score` decimal(10,2) DEFAULT NULL COMMENT '驾驶评分',
  `rank` smallint(6) DEFAULT NULL COMMENT '当日排名，百分比',
  PRIMARY KEY (`vin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='急加速急减速状态';

-- ----------------------------
-- Table structure for vehicle_abnormal_speed_stat_history
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_abnormal_speed_stat_history`;
CREATE TABLE `vehicle_abnormal_speed_stat_history` (
  `vin` varchar(30) NOT NULL COMMENT '车架号',
  `acc_on_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '引擎启动时间',
  `acc_off_time` datetime DEFAULT NULL COMMENT '引擎关闭时间',
  `speed_high_count` smallint(6) DEFAULT '0' COMMENT '急加速次数',
  `speed_low_count` smallint(6) DEFAULT '0' COMMENT '急减速次数',
  `over_speed_count` smallint(6) DEFAULT '0' COMMENT '超速次数',
  `score` decimal(10,2) DEFAULT NULL COMMENT '驾驶评分',
  `rank` smallint(6) DEFAULT NULL COMMENT '当日排名，百分比'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='急加速急减速历史状态';

-- ----------------------------
-- Table structure for vehicle_gps_log
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_gps_log`;
CREATE TABLE `vehicle_gps_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `vin` varchar(30) NOT NULL COMMENT 'vin码',
  `obd_id` varchar(50) DEFAULT NULL COMMENT 'OBD编号',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT NULL COMMENT '纬度',
  `speed` varchar(10) DEFAULT NULL COMMENT '速度',
  `engine_speed` varchar(10) DEFAULT NULL COMMENT '引擎转速',
  `gps_stat` varchar(20) DEFAULT NULL COMMENT 'GPS状态',
  `client_time` datetime DEFAULT NULL COMMENT 'gps时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '服务器时间',
  `coolant` varchar(10) DEFAULT NULL COMMENT '水温',
  `intakeMAP` varchar(10) DEFAULT NULL COMMENT '进气压力',
  `intakeAir` varchar(10) DEFAULT NULL COMMENT '进气温度',
  `absolute_throttle` varchar(10) DEFAULT NULL COMMENT '节气门开度',
  PRIMARY KEY (`id`),
  KEY `obd-create_time` (`obd_id`,`create_time`)
) ENGINE=InnoDB AUTO_INCREMENT=289250194 DEFAULT CHARSET=utf8 COMMENT='gps记录';

-- ----------------------------
-- Table structure for vehicle_latest_gps
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_latest_gps`;
CREATE TABLE `vehicle_latest_gps` (
  `vin` varchar(30) DEFAULT NULL COMMENT '车架号',
  `obd_id` varchar(50) NOT NULL COMMENT 'OBD设备id',
  `longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(30) DEFAULT NULL COMMENT '纬度',
  `speed` varchar(10) DEFAULT NULL COMMENT '速度',
  `engine_speed` varchar(10) DEFAULT NULL COMMENT '转速',
  `gps_stat` varchar(20) DEFAULT NULL COMMENT 'GPS状态',
  `client_time` datetime DEFAULT NULL COMMENT '客户端时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '服务器端创建时间',
  PRIMARY KEY (`obd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='车辆最新位置';

-- ----------------------------
-- Table structure for vehicle_latest_status
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_latest_status`;
CREATE TABLE `vehicle_latest_status` (
  `vin` varchar(30) NOT NULL COMMENT '车架号',
  `item_key` varchar(30) DEFAULT NULL COMMENT '键名',
  `item_value` varchar(30) DEFAULT NULL COMMENT '键值',
  `client_time` datetime DEFAULT NULL COMMENT '客户端时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '服务器端创建时间',
  UNIQUE KEY `ak_key_1` (`vin`,`item_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='车辆最新状态表';

-- ----------------------------
-- Table structure for vehicle_mileage
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_mileage`;
CREATE TABLE `vehicle_mileage` (
  `vin` varchar(30) NOT NULL COMMENT 'è½¦æž¶å·',
  `report_date` date DEFAULT NULL COMMENT 'ä¸ŠæŠ¥æ—¥æœŸ',
  `total_km` int(11) DEFAULT '0' COMMENT 'é‡Œç¨‹æ•°',
  `today_km` int(11) DEFAULT '0' COMMENT 'æœ¬æ—¥é‡Œç¨‹',
  `week_km` int(11) DEFAULT '0' COMMENT 'æœ¬å‘¨é‡Œç¨‹',
  `month_km` int(11) DEFAULT '0' COMMENT 'æœ¬æœˆé‡Œç¨‹',
  KEY `index_1` (`vin`,`report_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='è½¦è¾†è¡Œé©¶é‡Œç¨‹ï¼Œæˆªæ­¢åˆ°æŸä¸€æ—¥çš„æ€»è¡Œé©¶é‡Œç¨‹';

-- ----------------------------
-- Table structure for vehicle_runout_stat
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_runout_stat`;
CREATE TABLE `vehicle_runout_stat` (
  `vin` varchar(30) NOT NULL COMMENT '车架号',
  `base_longitude` varchar(30) DEFAULT NULL COMMENT '电子围栏经度',
  `base_latitude` varchar(30) DEFAULT NULL COMMENT '电子围栏维度',
  `base_range` int(11) DEFAULT NULL COMMENT '电子围栏距离',
  `out_stat` tinyint(1) DEFAULT '1' COMMENT '出栏是否已发送',
  `in_stat` tinyint(1) DEFAULT '0' COMMENT '入栏是否已触发',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '数据更新时间',
  PRIMARY KEY (`vin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='初始版电子围栏表（已废弃，由t_address_book代替）';

-- ----------------------------
-- Table structure for vehicle_runout_stat_test
-- ----------------------------
DROP TABLE IF EXISTS `vehicle_runout_stat_test`;
CREATE TABLE `vehicle_runout_stat_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vin` varchar(30) NOT NULL COMMENT 'vincode',
  `base_longitude` varchar(30) DEFAULT NULL COMMENT '经度',
  `base_latitude` varchar(30) DEFAULT NULL COMMENT '维度',
  `base_range` int(11) DEFAULT NULL COMMENT '半径',
  `out_stat` tinyint(1) DEFAULT '1' COMMENT '是否出栏',
  `in_stat` tinyint(1) DEFAULT '0' COMMENT '是否入栏',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`,`vin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for water_area
-- ----------------------------
DROP TABLE IF EXISTS `water_area`;
CREATE TABLE `water_area` (
  `id` int(11) NOT NULL DEFAULT '0',
  `cj` varchar(50) DEFAULT NULL COMMENT '厂家',
  `nk` varchar(20) DEFAULT NULL COMMENT '年款',
  `auto` varchar(10) DEFAULT 'hand' COMMENT '手动,自动',
  `pp` varchar(50) DEFAULT NULL COMMENT '品牌',
  `cx` varchar(50) DEFAULT NULL COMMENT '车型',
  `pl` float DEFAULT NULL COMMENT '排量',
  `low` int(10) DEFAULT '0' COMMENT '统计值',
  `high` int(8) DEFAULT NULL,
  `obdcount` int(8) DEFAULT NULL,
  `daycount` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Procedure structure for colfire
-- ----------------------------
DROP PROCEDURE IF EXISTS `colfire`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `colfire`(in dif int)
BEGIN
	declare _done1 int;
	declare _time1 datetime;
	declare _msg varchar(5);
	declare _obd varchar(30);
	declare _cont varchar(800);
	declare _id1 int;

	declare cur1 cursor for 
		select client_time,   obd_id,message_content from device_status_log where id BETWEEN 24007144+dif and  24007144+dif+9999
		and (message_content like '%acc=>02%' or message_id = '2e' or message_content like '%acc=>00%')  order by id;

	declare continue HANDLER for not found set _done1 = 1;
	open cur1;
	cur_loop: loop
			set _done1 = 0;
			fetch cur1 into _time1,  _obd, _cont;
			if _done1 = 1 then 
				leave cur_loop;
			end if;

			if _cont like '%acc=>00%' then 
					insert into collidefire8( obd_id, stoptime ) value ( _obd, _time1 );
			elseif  _cont like '%acc=>02%' then 
					set _id1 = null ;
					select id into _id1 from collidefire8 where obd_id = _obd and collide is not null  order by id desc limit 1;
					if _id1 is not null then 
						update collidefire8 set fire = _time1 where id = _id1; 
					end if;
			else 
					set _id1 = null ;
					select id into _id1 from collidefire8 where obd_id = _obd and fire is null order by id desc limit 1;
					if _id1 is not null then 
						update collidefire8 set collide = _time1 where id = _id1; 
					end if;
			end if; 

	end loop;
	close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for colfire1
-- ----------------------------
DROP PROCEDURE IF EXISTS `colfire1`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `colfire1`(in init int)
BEGIN
	declare _done1 int;
	declare _time1 datetime;
	declare _msg varchar(5);
	declare _obd varchar(30);
	declare _cont varchar(800);
	declare _id1 int;

	declare cur1 cursor for 
		select create_time,   obd_id,message_content from device_status_log where id BETWEEN 24007144+init and  24007144+init+9999
		and (message_content like '%acc=>02%' or message_content like '%theftDetect=>01%' /* or message_content like '%acc=>00%'*/)  order by id;

	declare continue HANDLER for not found set _done1 = 1;
	open cur1;
	cur_loop: loop
			set _done1 = 0;
			fetch cur1 into _time1,  _obd, _cont;
			if _done1 = 1 then 
				leave cur_loop;
			end if;

/*
			if _cont like '%acc=>00%' then 
					insert into collidefire8( obd_id, stoptime ) value ( _obd, _time1 );
			elseif  _cont like '%acc=>02%' then 
					set _id1 = null ;
					select id into _id1 from collidefire8 where obd_id = _obd and collide is not null  order by id desc limit 1;
					if _id1 is not null then 
						update collidefire8 set fire = _time1 where id = _id1; 
					end if;
			else 
					set _id1 = null ;
					select id into _id1 from collidefire8 where obd_id = _obd and fire is null order by id desc limit 1;
					if _id1 is not null then 
						update collidefire8 set collide = _time1 where id = _id1; 
					end if;
			end if; 
*/

			if _cont like '%theftDetect=>01%' then 
					insert into collidefire8( obd_id, collide ) value ( _obd, _time1 ); 			 
			else 
					set _id1 = null ;
					select id into _id1 from collidefire8 where obd_id = _obd and fire is null order by id desc limit 1;
					if _id1 is not null then 
						update collidefire8 set fire = _time1 where id = _id1; 
					end if;
			end if; 

	end loop;
	close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for colfire2
-- ----------------------------
DROP PROCEDURE IF EXISTS `colfire2`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `colfire2`(in init int)
begin 

declare _done1 int;
declare _done2 int;
declare _done3 int;
declare _id int;
declare _tid int;
declare _stop_time datetime;
declare _stop_len int;
declare _obd_id varchar(20);

declare _init_id int; 
declare _tmp_id1 int;
declare _tmp_id2 int;

declare _fire datetime;
declare _gps datetime;

declare obd_cur cursor for
	select id, obd_id, fire from collidefire8 where   id BETWEEN init and  init+9999 ;
	
declare continue handler for not found set _done1 = 1;

open obd_cur;
obd_cur_loop: loop

	set _done1 = 0;
	fetch obd_cur into _id,_obd_id, _fire;
	if _done1 = 1 then 
		leave obd_cur_loop;
	end if;	
 
		 
	begin 
		declare continue handler for not found set _done3 = 1;

		set _tmp_id1 = null;
		select minid into _tmp_id1 from table_id where tablename = 'vehicle_gps_log' 
 		and stat_time = str_to_date(concat( date( _fire),' ',hour( _fire)), '%Y-%m-%d %H');

		set _gps = null;
		select create_time into _gps 		from vehicle_gps_log 
		where obd_id = _obd_id and id >= _tmp_id1 and speed > 0		and create_time > _fire  limit 1;
		
	end ;			
			 
 update collidefire8 set gps= _gps where id = _id;

end loop;
close obd_cur;




end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for dddf
-- ----------------------------
DROP PROCEDURE IF EXISTS `dddf`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `dddf`()
begin 

declare _done1 int;
declare _done2 int;
declare _tid int;
declare _end_point varchar(1000);
declare _end_time datetime;
declare _obd_id varchar(50);
declare _longitude varchar(100);
declare _latitude varchar(100);
declare _last_logstop_id int;

declare obd_cur cursor for	select obd_id from botaiapp.t_obd;	
declare continue handler for not found set _done1 = 1;


select id into _last_logstop_id from log_stop order by id desc limit 1;

open obd_cur;
obd_cur_loop: loop
	
	set _done1 = 0;
	fetch obd_cur into _obd_id;
	if _done1 = 1 then 
		leave obd_cur_loop;
	end if;	
	
	set _done1 = 0;
	select tid into _tid from log_stop  where obd_id = _obd_id order by id desc limit 1;
		
	if _done1 = 1 then 
		ITERATE obd_cur_loop;
	end if;
 
	select end_point, end_time into _end_point, _end_time from locus_travel where id = _tid;

		set _end_point = split(_end_point, '|', 1);
			set _longitude = split(_end_point, ',', 1);
			set _latitude = split( _end_point, ',', 2);
 
		set _last_logstop_id = _last_logstop_id + 1;
		insert into log_stop(  id, obd_id, longitude, latitude, stop_time,  create_time, bid)
				values( _last_logstop_id, _obd_id, _longitude, _latitude, _end_time, now(), _tid) ;

end loop;
close obd_cur;
  
end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for locus_score_rank
-- ----------------------------
DROP PROCEDURE IF EXISTS `locus_score_rank`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `locus_score_rank`()
BEGIN
	
declare _total int;
declare _percentage int;
declare _done1 int;
declare _done2 int;
declare _sum int;
declare _target int;
declare _score int;
declare _amount int; 

declare cur1 cursor for select percentage from locus_score_rank;
DECLARE continue handler for not found set _done1 = 1;

select count(*) into _total from locus_score ;

drop table if exists tmp_locus_score_rank;
create table tmp_locus_score_rank as 
select score,count(*) as amount
from locus_score 
group by score order by score ;

open cur1;
cur1_loop: loop 
	set _done1 = 0;
	fetch cur1 into _percentage ;
	if _done1 = 1 then 
		leave cur1_loop;
	end if;

	set _target = floor( _total * _percentage / 100); 
	set _sum = 0; 
	begin 
		declare cur2 cursor for select score, amount from tmp_locus_score_rank;
		DECLARE continue handler for not found set _done2 = 1;
		open cur2;
		cur2_loop: loop
			set _done2 = 0;  
			fetch cur2 into _score, _amount;
			if _done2 = 1 then 
					leave cur2_loop;
			end if;

			set _sum = _sum + _amount;
			if _sum >= _target then 
					update locus_score_rank set score = _score where percentage = _percentage;				 
					leave cur2_loop;
			end if;
 
		end loop;
		close cur2;
	
	end;
end loop;
close cur1;

#drop table if exists tmp_locus_score_rank;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_spend
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_spend`;
DELIMITER ;;
CREATE DEFINER=`btapp`@`%` PROCEDURE `log_spend`(in init_id int)
BEGIN
	
declare _done1 int;
declare _collide int;
declare _id int;
declare _obd_id varchar(20);
declare _stop_time datetime;
declare _stop_len int;
declare _done2 int;
declare _id2 int;
 
declare cur1 cursor for select a.id,  obd_id, stop_time, stop_len from locus_analyse_stop a, log_spend b
	where b.id between init_id and init_id+9999 and b.id = a.id and stoptime is null;
	 
declare continue handler for not found set _done1 = 1;

open cur1; 

cur_loop:loop

	fetch cur1 into _id, _obd_id, _stop_time, _stop_len;
		update log_spend set stoptime = _stop_time where id = _id;
	if _done1 = 1 then 
		leave cur_loop;
	end if;

	set _collide = null;
	
	begin 
		declare continue handler for not found set _done2 = 1;
		
		set _done2 = 0;
		select minid into _id2 from table_id where tablename='device_status_log' and 
				stat_time = str_to_date(concat( date(_stop_time),' ',hour(_stop_time)), '%Y-%m-%d %H');
		
		if _done2 = 1 then 
		
			iterate cur_loop;
		end if;
		
		select id into _collide from device_status_log
		where 
		id >= _id2
		and message_content like '%theftDetect=>01%'
		and obd_id = _obd_id
		and create_time between _stop_time and date_add(_stop_time, interval _stop_len second)
		limit 1;
	end ;
	
	if _collide is null then 
		set _collide = -1;
	end if;
	
	if _stop_len between 120 and 1800 then 
		update log_spend set wash = _collide, care = '-1' where id = _id;
	elseif _stop_len > 1800 then 
		update log_spend set wash = '-1', care = _collide where id = _id;
	else 
		update log_spend set wash = '-1', care = '-1' where id = _id;
	end if;

end loop;
close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_spend27
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_spend27`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_spend27`(in init_id int)
BEGIN
	
declare _done1 int;
declare _collide int;
declare _id int;
declare _obd_id varchar(20);
declare _stop_time datetime;
declare _stop_len int;
declare _done2 int;
declare _id2 int;
 
declare cur1 cursor for select a.id,  obd_id, stop_time, stop_len from locus_analyse_stop a, log_spend b
	where b.id between init_id and init_id+9999 and b.id = a.id and stop27 is null;
	 
declare continue handler for not found set _done1 = 1;

open cur1; 

cur_loop:loop

	fetch cur1 into _id, _obd_id, _stop_time, _stop_len;
		update log_spend set stop27 = _stop_time where id = _id;
	if _done1 = 1 then 
		leave cur_loop;
	end if;

	set _collide = null;
	
	begin 
		declare continue handler for not found set _done2 = 1;
		
		set _done2 = 0;
		select minid into _id2 from table_id where tablename='device_status_log' and 
				stat_time = str_to_date(concat( date(_stop_time),' ',hour(_stop_time)), '%Y-%m-%d %H');
		
		if _done2 = 1 then 
		
			iterate cur_loop;
		end if;
		
		select sum(split(message_content,'>',2)) into _collide from device_status_log
		where 
		id >= _id2
		and message_id = '27'
		and obd_id = _obd_id
		and create_time between _stop_time and date_add(_stop_time, interval _stop_len second);
		#limit 1;
	end ;
	
	if _collide>= 0 and _stop_len between 120 and 1800 then 
		update log_spend set wash27 = _collide where id = _id;
	ELSE
		update log_spend set wash27 = -1 where id = _id;
	end if;
	
end loop;
close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_stop
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_stop`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_stop`()
begin 

declare _done1 int;
declare _done2 int;
declare _done3 int;
declare _sid int;
declare _tid int;
declare _stop_time datetime;
declare _stop_len int;
declare _end_point varchar(500);
declare _longitude varchar(50);
declare _latitude varchar(50);
declare _obd_id varchar(20);
declare _start_time datetime;
declare _end_time datetime;
declare _init_id int; 
declare _tmp_id2 int;

declare _upid bigint; 
declare _downid bigint;
declare _gps_stat varchar(5);

declare _last_logstop_id int;

declare obd_cur cursor for
#	select distinct obd_id from locus_travel; # where obd_id =  'P006000300000024';
	select obd_id from botaiapp.t_obd;
	
declare continue handler for not found set _done1 = 1;

select id into _last_logstop_id from log_stop order by id desc limit 1;

open obd_cur;
obd_cur_loop: loop
	
	set _done1 = 0;
	fetch obd_cur into _obd_id;
	if _done1 = 1 then 
		leave obd_cur_loop;
	end if;	
	
	set _done1 = 0;
	select tid into _init_id from log_stop  where obd_id = _obd_id order by id desc limit 1;
		
	if _done1 = 1 then 
	#	iterate obd_cur_loop;
		set _done1 = 0;
		select a.id into _init_id from locus_travel a,
				( select id from locus_travel order by id desc limit 1 ) b
				where obd_id = _obd_id and a.id > b.id - 2000 limit 1;

		if _done1 = 1 then 
			ITERATE obd_cur_loop;
		end if;
	end if;

	begin 
		declare travel_cur cursor for 
			select start_time, end_time, end_point, id from locus_travel where obd_id = _obd_id and id >= _init_id;
			
		declare continue handler for not found set _done2 = 1;
		
		open travel_cur;
		set _sid = null;		
		travel_loop: loop
			set _done2 = 0;
			fetch travel_cur into _start_time, _end_time, _end_point, _tid;
			if _done2 = 1 then 
				leave travel_loop;
			end if;
			
			if _sid is not null then 
			
				insert into log_stop( tid,  obd_id, longitude, latitude, stop_time, stop_len,create_time)
				values( _tid,  _obd_id, _longitude, _latitude, _stop_time,
				unix_timestamp(_start_time) - unix_timestamp(_stop_time),now());			
			
			end if;
	
			set _end_point = split(_end_point, '|', 1);
			set _longitude = split(_end_point, ',', 1);
			set _latitude = split( _end_point, ',', 2);
			set _sid = _tid;
			set _stop_time = _end_time;
			
			
			if _longitude is null or _latitude is null then 

			begin 
					declare continue handler for not found set _done3 = 1;
					set _done3 = 0;
					select id into _upid from vehicle_gps_log order by id desc limit 1;
					set _downid = _upid - 10000;
					while _longitude is null or _latitude is null do 

							set _gps_stat = null; set _tmp_id2 = null;

							select id into _tmp_id2 from vehicle_gps_log 	where obd_id = _obd_id 	and create_time < _end_time 
							and id BETWEEN _downid and _upid 		order by id desc limit 1;

							if _tmp_id2 is null then 
									set _upid = _downid -1; set _downid = _downid - 10000;
							else 				
								select longitude, latitude, gps_stat into _longitude, _latitude, _gps_stat from vehicle_gps_log where id = _tmp_id2 ;
									
								if 'A' != _gps_stat and 'S' != _gps_stat then 
									set _upid = _tmp_id2 - 1;
									set _downid = _tmp_id2 - 1000;
									set _longitude = null; set _latitude = null;
								end if;
							end if;
					end while;
				end ;			
			end if;
	
		end loop;
		close travel_cur;
	end;


end loop;
close obd_cur;


update log_stop set oil_name='-1', wash='-1',care='-1', wash27 = -1 where id in (
		select id from (
		select a.id from log_stop a, botaiapp.t_address_book b 
		where  a.id > _last_logstop_id - 5000 and   a.obd_id = b.obd_id and a.poi_address=b.address ) df );
 
update  log_stop set oil_name = '-1' where (stop_len < 120 or stop_len > 1800) and id > _last_logstop_id - 5000;

call log_stop_care(_last_logstop_id);
call log_stop_wash(_last_logstop_id);
 
end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_stop11
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_stop11`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_stop11`()
begin 

declare _done1 int;
declare _done2 int;
declare _done3 int;
declare _id int;
declare _tid int;
declare _stop_time datetime;
declare _stop_len int;
declare _end_point varchar(50);
declare _longitude varchar(20);
declare _latitude varchar(20);
declare _obd_id varchar(20);
declare _start_time datetime;
declare _end_time datetime;
declare _init_id int; 
declare _tmp_id1 int;
declare _tmp_id2 int;

declare obd_cur cursor for
	select id, obd_id, stop_time from log_stop where longitude is null or latitude is null;
	
declare continue handler for not found set _done1 = 1;

open obd_cur;
obd_cur_loop: loop

	fetch obd_cur into _id,_obd_id, _stop_time;
	if _done1 = 1 then 
		leave obd_cur_loop;
	end if;	
 
		set	 _longitude = null;
set  _latitude = null;
	begin 
					declare continue handler for not found set _done3 = 1;

		select minid into _tmp_id1 from table_id where tablename = 'vehicle_gps_log' 
		and stat_time = date_sub(_stop_time, interval second(_stop_time) + minute(_stop_time) * 60 + 3600 second);
					
			while _longitude is null or _latitude is null do 
					

					select id into _tmp_id2 
					from vehicle_gps_log 
					where obd_id = _obd_id and id >= _tmp_id1 
						and create_time < _stop_time order by id desc limit 1;
			
	select longitude, latitude into _longitude, _latitude from vehicle_gps_log  where id = _tmp_id2;

					set _tmp_id1 = _tmp_id1 - 10000;
			end while;
	
	end ;			
			 
 update log_stop set longitude = _longitude, latitude = _latitude where id = _id;


end loop;
close obd_cur;




end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_stop22
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_stop22`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_stop22`()
BEGIN
	
declare _done1 int;
declare _init_id  int;
declare _start_time datetime;
declare _end_time datetime;
declare _end_point varchar(200);
declare _obd_id varchar(20);
declare _id int;
declare _stop_time datetime;
declare _stop_len int;
declare _tmp_point varchar(100);
declare _log_stop_id int;


select minid into _init_id from table_id where tablename = 'locus_travel' and stat_time = '7000-1-1';
 
begin 
declare cur1 cursor for select start_time, end_time, end_point, obd_id, id 
from locus_travel where id BETWEEN _init_id and _init_id + 999;

declare continue HANDLER for not found set _done1 = 1;
open cur1;
cur_loop:loop
	fetch cur1 into _start_time, _end_time, _end_point, _obd_id, _id;
	if _done1 = 1 then 
		leave cur_loop;
	end if;

	select stop_time, stop_len , id  into _stop_time, _stop_len, _log_stop_id from log_stop where obd_id = _obd_id order by id desc limit 1;
	
	if stop_len is null and _stop_time <= _start_time then 
			set _tmp_point = split( _end_point, '|', 1);
			update log_stop set tid = _id, stop_len = UNIX_TIMESTAMP(_start_time) - UNIX_TIMESTAMP(_stop_time) where id = _log_stop_id;

			insert into log_stop(  sid , obd_id, longitude, latitude, stop_time , create_time) 
			values( _id, _obd_id, split(_tmp_point,',',1), split(_tmp_point,',',2), _end_time, now()); 

	end if;
end loop;
close cur1;

update table_id set minid = minid + 1000  where tablename = 'locus_travel' and stat_time = '7000-1-1'; 

end;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_stopp
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_stopp`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_stopp`()
begin 


declare _done1 int;
declare _done2 int;
declare _obd_id varchar(50);
declare _init_id int;
declare _tid int;
declare _id1 int;
declare _start_time datetime;
declare _end_time datetime;
declare _end_point varchar(500);
declare _longitude varchar(30);
declare _latitude varchar(30);
declare _stop_id int;
declare _last_logstop_id int;
declare _latest_id int;

declare obd_cur cursor for select obd_id from botaiapp.t_obd;
declare continue handler for not found set _done1 = 1;

select id into _last_logstop_id from log_stop order by id desc limit 1;
set _latest_id = _last_logstop_id;
 
open obd_cur;
obd_loop: loop
	
	set _done1 = 0;
	fetch obd_cur into _obd_id;
	if _done1 = 1 then 
		leave obd_loop;
	end if;
	
	set _done1 = 0;  # log_stop( tid,  obd_id, longitude, latitude, stop_time, stop_len,create_time)
	set _stop_id = null;
	select bid, id into _init_id, _stop_id from log_stop where obd_id = _obd_id order by id desc limit 1;
	if _done1 = 1 then 
	
		set _done1 = 0;
		select a.id-1 into _init_id from locus_travel a, ( select id from locus_travel order by id desc limit 1) b
		where a.id > b.id - 2000 and obd_id = _obd_id limit 1;
		
		if _done1 = 1 then 
			iterate obd_loop;
		end if;
	
	end if;
	
	begin 
		declare travel_cur cursor for select start_time, end_time, end_point, id  from locus_travel where obd_id = _obd_id and id > _init_id;
		declare continue handler for not found set _done2 = 1; 
		open travel_cur;
		travel_loop: loop
			set _done2 = 0;
			set _start_time = null; set _end_time = null ; set _end_point = null; set _id1 = null;
			fetch travel_cur into _start_time, _end_time, _end_point, _id1;
			if _done2 = 1 then 
				leave travel_loop;
			end if;

			update log_stop set stop_len = unix_timestamp(_start_time) - unix_timestamp(stop_time), tid = _id1 where id = _stop_id;
					
			set _end_point = split(_end_point, '|', 1);
			set _longitude = split(_end_point, ',', 1);
			set _latitude = split( _end_point, ',', 2);
			
			set _last_logstop_id = _last_logstop_id + 1;
			insert into log_stop( id,  bid, obd_id, longitude, latitude, stop_time, create_time)
			values( _last_logstop_id, _id1, _obd_id, _longitude, _latitude, _end_time, now());
			
			set _stop_id = _last_logstop_id;

		end loop;
		close travel_cur;
	end ;

end loop;
close obd_cur;


begin 
	declare lat_cur cursor for   
		select 	a.id, b.end_point
		from  log_stop a , locus_travel b , ( select id from log_stop order by id desc limit 1) c
		where  		a.id > c.id - 10000 and longitude is null and a.bid = b.id and b.end_point is not null ;

	declare continue handler for not found set _done2 = 1;
	open lat_cur;
	lat_loop: loop
			set _done2 = 0;
			fetch lat_cur into _id1, _end_point;
			if _done2 = 1 then 
				leave lat_loop;
			end if;
		
			set _end_point = split(_end_point, '|', 1);
			set _longitude = split(_end_point, ',', 1);
			set _latitude = split( _end_point, ',', 2);
			
			update log_stop set longitude = _longitude, latitude = _latitude where id = _id1;

	end loop;
	close lat_cur;

end;

update log_stop set oil_name='-1', wash='-1',care='-1', wash27 = -1 where stop_len is not null and  id in (
		select id from (
		select a.id from log_stop a, botaiapp.t_address_book b 
		where  a.id > _latest_id - 5000 and   a.obd_id = b.obd_id and a.poi_address=b.address ) df );
 
update  log_stop set oil_name = '-1' where (stop_len < 120 or stop_len > 1800) and id > _latest_id - 5000;

 
call log_stop_care(_latest_id);
call log_stop_wash(_latest_id);

end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_stop_care
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_stop_care`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_stop_care`(in _last int)
BEGIN
	
declare _done1 int;
declare _collide int;
declare _id int;
declare _obd_id varchar(20);
declare _stop_time datetime;
declare _stop_len int;
declare _done2 int;
declare _id2 int;
 
declare cur1 cursor for select id,  obd_id, stop_time, stop_len from log_stop
	where     #id between init_id and init_id+9999 and (
    (wash is null or care is null) and id > _last - 20000 and stop_len is not null ;
	 
declare continue handler for not found set _done1 = 1;

open cur1; 
cur_loop:loop

	fetch cur1 into _id, _obd_id, _stop_time, _stop_len;
		#update log_stop set stoptime = _stop_time where id = _id;
	if _done1 = 1 then 
		leave cur_loop;
	end if;

	set _collide = null;	
	begin 
		declare continue handler for not found set _done2 = 1;
		
		set _done2 = 0;
		select minid into _id2 from table_id where tablename='device_status_log' and 
				stat_time = str_to_date(concat( date(_stop_time),' ',hour(_stop_time)), '%Y-%m-%d %H');
		
		if _done2 = 1 then 	
		#	update log_stop set wash = '-5', care = '-5' where id = _id;
			iterate cur_loop;
		end if;
		
		select 1 into _collide from device_status_log
		where 
		id >= _id2
		and message_content like '%theftDetect=>01%'
		and obd_id = _obd_id
		and create_time between _stop_time and date_add(_stop_time, interval _stop_len second)
		limit 1;
	end ;
	
	if _collide is null then 
		set _collide = -1;
	end if;
	
	if _stop_len between 120 and 1800 then 
		update log_stop set wash = _collide, care = '-1' where id = _id;
	elseif _stop_len > 1800 then 
		update log_stop set wash = '-1', care = _collide where id = _id;
	else 
		update log_stop set wash = '-1', care = '-1' where id = _id;
	end if;

end loop;
close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for log_stop_wash
-- ----------------------------
DROP PROCEDURE IF EXISTS `log_stop_wash`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `log_stop_wash`(in _last  int)
BEGIN
	
declare _done1 int;
declare _collide int;
declare _id int;
declare _obd_id varchar(20);
declare _stop_time datetime;
declare _stop_len int;
declare _done2 int;
declare _id2 int;
 
declare cur1 cursor for select id,  obd_id, stop_time, stop_len from log_stop 
	where # b.id between init_id and init_id+9999 and b.id = a.id and 
	( care27 is null or	wash27 is null) and id > _last - 20000 and stop_len is not null;
	 
declare continue handler for not found set _done1 = 1;

open cur1; 

cur_loop:loop

	set _done1 = 0;
	fetch cur1 into _id, _obd_id, _stop_time, _stop_len;
		#update log_stop set stop27 = _stop_time where id = _id;
	if _done1 = 1 then 
		leave cur_loop;
	end if;

	set _collide = null;
	
	begin 
		declare continue handler for not found set _done2 = 1;
		
		set _done2 = 0;
		select minid into _id2 from table_id where tablename='device_status_log' and 
				stat_time = str_to_date(concat( date(_stop_time),' ',hour(_stop_time)), '%Y-%m-%d %H');
		
		if _done2 = 1 then 
		#	update log_stop set wash27 = -2 where id = _id;
			iterate cur_loop;
		end if;
		
		select sum(split(message_content,'>',2)) into _collide from device_status_log
		where 
		id >= _id2
		and message_id = '27'
		and obd_id = _obd_id
		and create_time between _stop_time and date_add(_stop_time, interval _stop_len second);
		#limit 1;
	end ;
	
	if _collide>= 0 and _stop_len between 120 and 1800 then 
		update log_stop set wash27 = _collide, care27 = -1 where id = _id;
	elseif _collide >= 0 and _stop_len > 1800 THEN
		update log_stop set wash27 = -1, care27 = _collide where id = _id;
	ELSE
		update log_stop set wash27 = -1, care27 = -1 where id = _id;
	end if;
	
end loop;
close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for obd_last_login
-- ----------------------------
DROP PROCEDURE IF EXISTS `obd_last_login`;
DELIMITER ;;
CREATE DEFINER=`btapp`@`%` PROCEDURE `obd_last_login`()
BEGIN
	
declare _done1 int;
declare _done2 int;
declare _last_id int;
declare _i2 int;
declare _obd_id varchar(80);
declare _dt1 datetime;
declare _dt2 datetime;

declare cur1 cursor for 
	select	DISTINCT obd_id from botaiapp.t_obd where uid > 0;
#	select distinct obd_id from botaiapp.t_user where obd_id is not null and obd_id != '';

declare continue handler for not found set _done1 = 1;

select id into _last_id from locus_travel order by id desc limit 1;
open cur1;
cur_loop: loop
begin
	fetch cur1 into _obd_id;
	if _done1 = 1 then
		leave cur_loop;
	end if;

	#	insert into obd_last_login (obd_id, lastdt, create_time) values( _obd_id, '8888-8-8','6666-6-6');
	begin 
		declare continue handler for not found set _done2 = 1;
		set _dt1 = null;
		set _i2 = _last_id ;
		set _dt2 = null;
		while _dt1 is null and _i2 > 0 do 

				select end_time,create_time into _dt1, _dt2 from locus_travel where id between _i2 - 10000 and _i2
					and obd_id = _obd_id 		order by id desc limit 1;
				set _i2 = _i2 - 10001;
		end while;

		insert into obd_last_login (obd_id, lastdt, create_time) values( _obd_id, _dt1,_dt2);
	end; 
end;

end loop;
close cur1;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for proc_collectdata
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_collectdata`;
DELIMITER ;;
CREATE DEFINER=`btapp`@`%` PROCEDURE `proc_collectdata`(
	in 	datatype				int, 
	in 	vin							varchar(30),
	in 	obd_id					varchar(50),
	in 	function_id			varchar(10),
	in 	message_id			varchar(10),
	in 	message_content	text,
	in 	longitude				varchar(50),
	in 	latitude				varchar(50),
	in 	speed						varchar(10),
	in 	engine_speed		varchar(10),
	in 	gps_stat				varchar(20),
	in 	client_time			datetime,
	in	coolant  varchar(10),
	in	intakeMAP  varchar(10),
	in	intakeAir  varchar(10),
	in	absolute_throttle  varchar(10)
)
begin
		/*
		datatype：
		0，车辆位置信息；
		1，车况信息；
	*/
	if(datatype = 1)then
		set @strvin = "";
		set @stmvin = "";

		set @strvin = concat('insert into device_status_log (vin, obd_id, function_id, message_id, message_content, longitude, latitude, speed, engine_speed, gps_stat, client_time) values (''', vin, ''', ''', obd_id, ''', ''', function_id, ''', ''', message_id, ''', ''', message_content, ''', ''', longitude, ''', ''', latitude, ''', ''', speed, ''', ''', engine_speed, ''', ''', gps_stat, ''', ''', client_time, ''')');
		prepare stmvin from @strvin;
		execute stmvin;
	end if;

	if((longitude is not null) and (latitude is not null) and (cast(longitude as signed) > 0) and (cast(latitude as signed) > 0))then
		set @strgps = "";
		set @stmgps = "";

		-- set @strgps = concat('insert into vehicle_gps_log (vin, obd_id, longitude, latitude, speed, engine_speed, gps_stat, client_time) values (''', vin, ''', ''', obd_id, ''', ''', longitude, ''', ''', latitude, ''', ''', speed, ''', ''', engine_speed, ''', ''', gps_stat, ''', ''', client_time, ''')');
		set @strgps = concat('insert into vehicle_gps_log (vin, obd_id, longitude, latitude, speed, engine_speed, gps_stat, client_time,coolant,intakeMAP,intakeAir,absolute_throttle) values (''', vin, ''', ''', obd_id, ''', ''', longitude, ''', ''', latitude, ''', ''', speed, ''', ''', engine_speed, ''', ''', gps_stat, ''', ''', client_time, ''', ''', coolant, ''', ''', intakeMAP, ''', ''', intakeAir, ''', ''', absolute_throttle, ''')');
		-- select @strgps;
		prepare stmgps from @strgps;
		execute stmgps;
	end if;
end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for refreshTableId
-- ----------------------------
DROP PROCEDURE IF EXISTS `refreshTableId`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `refreshTableId`()
BEGIN
	
declare _id1 int;
declare _dt datetime;


select minid, stat_time into _id1, _dt from table_id where tablename = 'vehicle_gps_log'  order by stat_time desc limit 1;

insert into table_id ( tablename, stat_time, minid)
select  'vehicle_gps_log', str_to_date(concat( date(create_time),' ',hour(create_time)), '%Y-%m-%d %H') as d,min(id) as mid 
from vehicle_gps_log where id > _id1  and create_time >= date_add( _dt, interval 1 hour)  group by d ;



select minid, stat_time into _id1, _dt from table_id where tablename = 'device_status_log'  
and stat_time < '3000-1-1' order by stat_time desc limit 1;

insert into table_id ( tablename, stat_time, minid)
select  'device_status_log', str_to_date(concat( date(create_time),' ',hour(create_time)), '%Y-%m-%d %H') as d,min(id) as mid 
from device_status_log where id > _id1  and create_time >= date_add( _dt, interval 1 hour)  group by d ;


 

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for stay_log
-- ----------------------------
DROP PROCEDURE IF EXISTS `stay_log`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `stay_log`()
begin

declare _init_id int;
declare _last_id int;
declare _done1 int;
declare _done2 int;
declare _lng varchar(30);
declare _lat varchar(30);
declare _obd_id varchar(50);
declare _client_time datetime;
declare _create_time datetime;
declare _fire_tag varchar(10);
declare _gps_stat varchar(10);
 
declare _i1 int;
declare _i2 int;
declare _i3 int;
declare _dt1 datetime;
declare _dt2 datetime;


select minid into _init_id from table_id where tablename='device_status_log' and stat_time='7777-7-7';
select id into _last_id from device_status_log order by id desc limit 1;

if _last_id > _init_id + 10000 then 
	set _last_id = _init_id + 10000;
end if;


begin 
	declare fire_cursor cursor FOR
	select  obd_id, client_time, create_time, case when message_content like '%acc=>02%' then 'startcar' 	else 'stopcar' end fire_tag
	from device_status_log
	where id BETWEEN _init_id and _last_id 	and ( message_content like '%acc=>02%' or message_content like '%acc=>00%' )
	order by obd_id, id;

	declare continue handler for not found set _done1 = 1;
	set _done1 = 0;
	open fire_cursor;
	fire_loop: loop
		fetch fire_cursor into _obd_id, _client_time, _create_time, _fire_tag;
		if _done1 = 1 then 
			leave fire_loop;
		end if; 
		
		begin 
			declare continue handler for not found set _done2 = 1;
			
			if _fire_tag = 'stopcar' THEN
				# find latest gps
				#id	obd_id	longitude	latitude	stop_client_time	stop_create_time	start_client_time	start_create_time	duration	oil_name	#collide	class

				set _lng = null;
				set _lat = null;
				set _i1 = null;
				set _dt1 = null;
				set _dt2 = null;
				set _i3 = null;
				set _gps_stat = null;
/*
				select minid into _i1
				from table_id where tablename='vehicle_gps_log' and stat_time = str_to_date(concat( date(_create_time),' ',hour(_create_time)), '%Y-%m-%d %H') ;
				
				select id into _i3
				from vehicle_gps_log where id >= _i1  #and gps_stat in ('A', 'S')
				and obd_id = _obd_id and create_time < _create_time order by id desc limit 1;
				
				select longitude, latitude, client_time, create_time, gps_stat into _lng, _lat, _dt1,_dt2, _gps_stat
				from vehicle_gps_log where id = _i3;

				set _dt1 = _create_time;
				while _lng is null
					and unix_timestamp(_create_time) - unix_timestamp(_dt1) < 259200
				do
					set _i1 = _i1 - 10000;
					set _i3 = null;

					select id into _i3
					from vehicle_gps_log where id between _i1 and _i1+9999 and obd_id = _obd_id and create_time < _create_time order by id desc limit 1;

					select longitude, latitude, client_time, create_time, gps_stat into _lng, _lat,_dt1,_dt2, _gps_stat
					from vehicle_gps_log where id = _i3;
					
					select create_time into _dt1 from vehicle_gps_log where id = _i1;
				end while;
*/			
				insert into stay_log(obd_id, longitude, latitude, gps_client_time, gps_create_time, gps_stat, stop_client_time, stop_create_time,stop_now)
				values( _obd_id, _lng, _lat, _dt1,_dt2, _gps_stat, _client_time, _create_time, now());
			
			else 
			
				# start 
				#id	obd_id	longitude	latitude	stop_client_time	stop_create_time	start_client_time	start_create_time	duration	oil_name	#collide	class
 				
				select id, start_create_time into _i1,_dt1 	from stay_log where obd_id = _obd_id order by id desc limit 1;
				
				if _dt1 is null then 
		/*		
					select minid into _i2
					from table_id where tablename='device_status_log' and	stat_time = str_to_date(concat( date(_dt1),' ',hour(_dt1)), '%Y-%m-%d %H') ;
				
					select 1 into _i3 
					from device_status_log where id > _i2 and obd_id = _obd_id and message_content like '%theftDetect=>01%'
					and create_time between _dt1 and _create_time limit 1;
			*/	
					update stay_log set start_client_time = _client_time, start_create_time = _create_time,  # collide = _i3, start_now = now(),
					duration = unix_timestamp(_client_time) - unix_timestamp( stop_client_time ) where id = _i1;
				
				end if; 
 		 

			end if;
		
		end;
	end loop;
	close fire_cursor;

	update table_id set minid = _last_id+1 where tablename='device_status_log' and stat_time='7777-7-7';

end; 
end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for t1
-- ----------------------------
DROP PROCEDURE IF EXISTS `t1`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `t1`()
begin

declare stat_day date;
DECLARE i int;

set stat_day = '2014-11-2';

set i = 0; 
while i < 20
do
	
	call gps_delay(stat_day);
#	call chkWash( stat_day );
 
#	call chkAddOil( stat_day );
#	call travelDelay(stat_day);
# call collideMsgDelay(stat_day);

# call gpsDelay( stat_day );
# call firstGpsDelay( stat_day );


set stat_day = DATE_ADD( stat_day , INTERVAL - 1 day ) ;
set i = i + 1;

end while;
 
end
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for t2
-- ----------------------------
DROP PROCEDURE IF EXISTS `t2`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` PROCEDURE `t2`()
BEGIN	 
declare _i int;
declare _init_id int;

#set _init_id = 1900000;
set _i =12; #17; 
while _i < 18 do
	
#	call battery_decay();
#	call fire_travel();
#	call stay_log();

#	call log_spend27(_init_id);

	#set _init_id = _init_id + 10000;
	
#	call log_stop22();
	call colfire2(_i*10000);
	set _i = _i + 1;
end while;

END
;;
DELIMITER ;

-- ----------------------------
-- Function structure for gps_distance
-- ----------------------------
DROP FUNCTION IF EXISTS `gps_distance`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` FUNCTION `gps_distance`(f_lng1 varchar(30),f_lat1 varchar(30),f_lng2 varchar(30),f_lat2 varchar(30)) RETURNS double(25,15)
BEGIN
	
	DECLARE _start varchar(70);
	DECLARE _end  varchar(70);
	DECLARE _x1 varchar(30);
	DECLARE _y1 varchar(30);
	DECLARE _x2 varchar(30);
	DECLARE _y2 varchar(30); 
	declare radius int;
	declare lat1 double(25,15);
	declare lng1 double(25,15);
	declare lat2 double(25,15);
	declare lng2 double(25,15);

	declare calcLongitude double(30,20);
	declare calcLatitude double(30,20);
	declare stepone double(30,20);
	declare steptwo double(30,20);
	declare d double(10,1);

	set _x1 = split(f_lng1,'+', 2);	
	set _y1 = split(f_lat1,'+',2);
 
	set _x2 = split(f_lng2,'+',2);	
	set _y2 = split(f_lat2,'+',2); 
  
	set radius = 6378140;    
	set lat1 = (_y1*pi())/180;   
	set lng1 = (_x1*pi())/180;  
	set lat2 = (_y2*pi())/180; 
	set lng2 = (_x2*pi())/180;
	set calcLongitude = lng2 - lng1;
	set calcLatitude = lat2 - lat1;
  
	set stepone = pow(sin(calcLatitude / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(calcLongitude / 2), 2); 

	set steptwo = sqrt(stepone);
	if 1 < steptwo THEN
		set steptwo = 1;
	end if;

	set steptwo = 2 * asin( steptwo );   
 
	set d = radius * steptwo; 
	if d > 200000 THEN
		set d = 0;
	end if;

	return round(d*10)/10;
  
END
;;
DELIMITER ;

-- ----------------------------
-- Function structure for lat_long_distance
-- ----------------------------
DROP FUNCTION IF EXISTS `lat_long_distance`;
DELIMITER ;;
CREATE DEFINER=`fajing`@`%` FUNCTION `lat_long_distance`(in_lat1 DOUBLE, in_long1 DOUBLE, in_lat_long2 VARCHAR(255)) RETURNS double
BEGIN
    DECLARE Distance DOUBLE;

    DECLARE RadLatBegin DOUBLE;
    DECLARE RadLatEnd DOUBLE;
    DECLARE RadLatDiff DOUBLE;
    DECLARE RadLngDiff DOUBLE;
    DECLARE in_lat2 DOUBLE;
    DECLARE in_long2 DOUBLE;

    DECLARE EARTH_RADIUS DOUBLE;
    SET EARTH_RADIUS = 6378.137;

    SET in_long2 = CONVERT(SUBSTRING(in_lat_long2, 1, POSITION(',' in in_lat_long2) -1), 
              DECIMAL(18,12));
    SET in_lat2 = CONVERT( SUBSTRING(in_lat_long2, POSITION(',' in in_lat_long2) + 1,
     POSITION('|' in in_lat_long2) - POSITION(',' in in_lat_long2) -1), DECIMAL(18,12));

    SET RadLatBegin = in_lat1 *PI()/ 180.0 ;
    SET RadLatEnd = in_lat2 *PI()/ 180.0 ;
    SET RadLatDiff = RadLatBegin - RadLatEnd;
    SET RadLngDiff = in_long1 *PI()/ 180.0 - in_long2 *PI()/ 180.0 ;
    SET DISTANCE = 2 *ASIN(
               SQRT(
                   POWER(SIN(RadLatDiff / 2), 2)+COS(RadLatBegin)*COS(RadLatEnd) 
                   *POWER(SIN(RadLngDiff / 2), 2)
               )
           );
       
    SET Distance = Distance * EARTH_RADIUS;
RETURN DISTANCE;
END
;;
DELIMITER ;

-- ----------------------------
-- Function structure for split
-- ----------------------------
DROP FUNCTION IF EXISTS `split`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` FUNCTION `split`(  
f_string varchar(1000),f_delimiter varchar(5),f_order int) RETURNS varchar(255) CHARSET utf8
BEGIN  
  declare result varchar(255) default '';  
  set result = reverse(substring_index(reverse(substring_index(f_string,f_delimiter,f_order)),f_delimiter,1));  
  return result;  
END
;;
DELIMITER ;

-- ----------------------------
-- Event structure for calStayLog
-- ----------------------------
DROP EVENT IF EXISTS `calStayLog`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` EVENT `calStayLog` ON SCHEDULE EVERY 1 YEAR STARTS '2014-11-13 19:06:14' ON COMPLETION PRESERVE DISABLE DO call t2()
;;
DELIMITER ;

-- ----------------------------
-- Event structure for refreshTableId
-- ----------------------------
DROP EVENT IF EXISTS `refreshTableId`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` EVENT `refreshTableId` ON SCHEDULE EVERY 30 MINUTE STARTS '2014-11-28 17:38:00' ON COMPLETION PRESERVE ENABLE DO call refreshTableId()
;;
DELIMITER ;

-- ----------------------------
-- Event structure for refrshLogStop
-- ----------------------------
DROP EVENT IF EXISTS `refrshLogStop`;
DELIMITER ;;
CREATE DEFINER=`cyh`@`%` EVENT `refrshLogStop` ON SCHEDULE EVERY 120 MINUTE STARTS '2014-11-28 17:35:35' ON COMPLETION PRESERVE ENABLE DO call log_stop()
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `trig_device_status_log_ai`;
DELIMITER ;;
CREATE TRIGGER `trig_device_status_log_ai` AFTER INSERT ON `device_status_log` FOR EACH ROW begin
	if (new.message_content is not null and new.message_content <> '') then
#		if(new.vin is null or new.vin = '')then #这一段写上去后，log日志会报错
#		update device_status_log
# 		set vin = new.obd_id
# 		where create_time = new.create_time
# 		and		obd_id = new.obd_id;
#		new.vin = new.obd_id;
#		end if;
#		0606把2e改为2a判断激活消息
		if(new.message_id = '2a')then
#			激活消息下发
			set @tmp_active_time = null;

			select 
				active_time into @tmp_active_time 
			from obd_latest_status 
			where obd_id = new.obd_id;

			if (@tmp_active_time is null) then
#				检查是否有激活消息
#				set @stractive = false;
#				select new.message_content REGEXP 'activated=>31' into @stractive;
				if(new.message_content REGEXP 'activated=>31')then
					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 0, 0, '提醒', 'MiniX 已经激活', 'iVokaMINI X 激活成功！', '恭喜', null, null, 'Active');

#					获取字符串中的数据
					replace into obd_latest_status (obd_id, vin, active_time, client_time) values (new.obd_id, new.vin, now(), new.client_time);
				end if;
			end if;
		end if;

		if(new.message_id = '2e')then
#                                        modify by yuhaiyang for lost connectioin
                                          replace into device_latest_e2 (id, vin, obd_id, function_id, message_id, message_content, longitude, latitude, speed, engine_speed, gps_stat, client_time, update_time, analytical_result) values (new.id, new.vin, new.obd_id, new.function_id, new.message_id, new.message_content, new.longitude, new.latitude, new.speed, new.engine_speed, new.gps_stat, new.client_time, now(), new.analytical_result); 
			if((new.message_content REGEXP 'softwareVersion=>') and (new.message_content REGEXP 'hardwareVersion=>'))then
#				OBD 软件版本获取
				set @tmp_sstr = null;			
				set @tmp_sver = null;
				select substring(new.message_content, position('softwareVersion=>' in new.message_content) + length('softwareVersion=>')) into @tmp_sstr;

				select substring(@tmp_sstr, 1, position(',' in @tmp_sstr) - 1) into @tmp_sver;
#				select substring(@tmp_sstr, 1, 2) into @tmp_sver;

				set @tmp_hstr = null;
				set @tmp_hver = null;
				select substring(new.message_content, position('hardwareVersion=>' in new.message_content) + length('hardwareVersion=>')) into @tmp_hstr;

				select substring(@tmp_hstr, 1, position(',' in @tmp_hstr) - 1) into @tmp_hver;
#				select substring(@tmp_hstr, 1, 2) into @tmp_hver;

				update obd_latest_status 
					set soft_ver = @tmp_sver,
						hard_ver = @tmp_hver,
						update_time = now()
				where obd_id = new.obd_id;
			end if;
		end if;

		if(new.message_id = '2f')then

#			插入行程开始时间
			if(new.message_content REGEXP 'acc=>02')then
				replace into message_track_log (obd_id,start_time) values (new.obd_id,new.create_time);
#			重置状态，如果看到引擎点火,重置状态				
				replace into vehicle_abnormal_speed_stat (vin) values (new.obd_id);
			end if;
			
#			计算急加速及减速次数
#			增加急加速次数
			if(new.message_content REGEXP 'speed=>02')then
				update vehicle_abnormal_speed_stat set speed_high_count = speed_high_count + 1 where vin = new.obd_id;
#				增加急加速消息通知(Evan)
#				insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude) values (new.vin, new.obd_id, 2, 1, '警报', '您的爱车在', now(), '急加速一次', null, null);
			end if;

#			增加急减速次数
			if(new.message_content REGEXP 'speed=>01')then
				update vehicle_abnormal_speed_stat set speed_low_count = speed_low_count + 1 where vin = new.obd_id;
#				增加急刹车消息通知(Evan)
#				insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude) values (new.vin, new.obd_id, 2, 1, '警报', '您的爱车在', now(), '急刹一次', null, null);
			end if;

#			只更新熄火时间字段
			if(new.message_content REGEXP 'acc=>00')then
#				和异常移动区分开来
				if(new.message_content REGEXP 'theftDetect=>00')then
#					更新行程结束时间
					update message_track_log set end_time = new.create_time where obd_id = new.obd_id;
					update vehicle_abnormal_speed_stat set acc_off_time = new.client_time where vin = new.obd_id;
#					行程结束后发送急加速急减速超速信息
#					set @aup = 0;
#					set @adown = 0;
#					set @accl = 0;
#					select speed_high_count,speed_low_count,over_speed_count into @aup,@adown,@accl from vehicle_abnormal_speed_stat where vin = new.obd_id;
#					select speed_up,speed_down,highspeed_count into @aup,@adown,@accl from locus_travel where obd_id = new.obd_id and mileage > 0 order by id desc limit 1;
#					由于从季恩那边取实时消息有延迟，所以现在只推实时的急加速急减速，超速先不推 2014/7/10
#					select speed_high_count,speed_low_count,over_speed_count into @aup,@adown,@accl from vehicle_abnormal_speed_stat where vin = new.obd_id;
#					if(@aup > 0) then
#						insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 2, 0, '提醒', '您的爱车', concat('本次行程急加速',@aup,'次'),null, null, null, 'Speed');
#					end if;
#					if(@adown > 0) then
#						insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 2, 0, '提醒', '您的爱车', concat('本次行程急减速',@adown,'次'),null, null, null, 'Skid');
#					end if;
#					if(@accl > 0) then
#						insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 2, 2, '提醒', '您的爱车', concat('本次行程超速',@accl,'次'),null, null, null, 'Speeding');
#					end if;
#					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude) values (new.vin, new.obd_id, 2, 1, '警报', '您的爱车在', now(), '急刹一次', null, null);
							
#					获取驾驶评分
#					update vehicle_abnormal_speed_stat set acc_off_time = new.client_time, score = if((truncate((unix_timestamp(acc_off_time) - unix_timestamp(acc_on_time))/60, 0) - (speed_high_count + speed_low_count*1.5)*10) < 0, 0, (truncate((unix_timestamp(acc_off_time) - unix_timestamp(acc_on_time))/60, 0) - (speed_high_count + speed_low_count*1.5)*10)) where vin = new.obd_id;
#	
#					获取驾驶排名；此处放在触发器中，性能堪忧啊，最后还是最好异步处理。
#					set @max_score = 1;
#					select max(score) into @max_score from vehicle_abnormal_speed_stat where date(acc_on_time) = date(now());
#					if(@max_score <= 0)then
#						set @max_score = 1;
#					end if;
#					update vehicle_abnormal_speed_stat set rank = (score/@max_score)*100 where date(acc_on_time) = date(now());

#					写入历史表
					insert into vehicle_abnormal_speed_stat_history select * from vehicle_abnormal_speed_stat where vin = new.obd_id;
				end if;
			end if;

#			获取车辆异常移动
#			if(new.message_content REGEXP 'theftDetect=>01')then
#				insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 2, 1, '警报', '您的爱车有', '异常移动', '请检查', null, null, 'AbnormalMovement');
#			end if;
#			更改电压获取逻辑0815
#			将电压信息放入车辆最新状态表
			delete from vehicle_latest_status where vin = new.vin and item_key = 'battery_stat';
			
			if(new.message_content REGEXP 'carBattery=>01')then
				set @epressure = 0;
				select CONV(SUBSTR(new.message_content,POSITION('carBatteryValue=>' IN new.message_content)+LENGTH('carBatteryValue=>'),2),16,10)/10 into @epressure;
				if( @epressure < 11.6 ) then
					set @bgps_lng = null;
					set @bgps_lat = null;
					select longitude,latitude into @bgps_lng,@bgps_lat from obdvin_log.vehicle_latest_gps where gps_stat='A' and obd_id=new.obd_id;
					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 1, 1, '提醒', '您的爱车', concat('电压过低，剩余|',@epressure,'|伏'), '请检查', @bgps_lng, @bgps_lat, 'BatteryLow');
				end if;
				replace into vehicle_latest_status (vin, item_key, item_value, client_time) values (new.vin, 'battery_stat', concat('low',@epressure), new.client_time);
			end if;
#			获取电压低
#			if((new.message_content REGEXP 'carBattery=>01') and (new.message_content REGEXP 'acc=>00'))then
#				insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 0, '提醒', '您的爱车', '电压过低', '请检查', null, null, 'BatteryLow');

#				低电压状态
#				replace into vehicle_latest_status (vin, item_key, item_value, client_time) values (new.vin, 'battery_stat', 'low', new.client_time);
#			end if;
#			正常电压状态
			replace into vehicle_latest_status (vin, item_key, item_value, client_time) values (new.vin, 'battery_stat', 'comm', new.client_time);
#			增加水温异常消息通知(Evan)
			#if(new.message_content REGEXP 'waterAlarm=>01')then
			#	set @water_send = 0;
			#	set @water_etime = '';
			#	select end_time,water_send_status into @water_etime,@water_send from message_track_log where obd_id = new.obd_id;
			#	if(@water_send = 0 and @water_etime is null) then
			#		insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 1, 1, '警报', '您的爱车在', CONCAT(DATE_FORMAT(NOW(),'%H:%i'), '水温异常'),'请检查', null, null, 'WaterAberrant');
			#		update message_track_log set water_send_status = 1 where obd_id = new.obd_id;
			#	end if;
			#end if;
		end if;

#		if(new.message_id = '30')then
##			算油量
#			if((new.message_content REGEXP '"2f":"') and (new.message_content REGEXP 'uploadState=>30'))then
#				set @oil_stat = null;
#				set @oil_value = '';
#				select substring(new.message_content, position('"2f":"' in new.message_content) + length('"2f":"'), 2) into @oil_value;
#				if(@oil_value <> '0c')then
#					select truncate((conv(@oil_value, 16, 10)*100/255), 1) into @oil_stat;
#					
#	#				一次行程只发一次
#					set @oil_send = 0;
#					set @oil_etime = '';
#					select end_time,oil_send_status into @oil_etime,@oil_send from message_track_log where obd_id = new.obd_id;
#					if(@oil_stat is not null and @oil_stat < 10 and @oil_send = 0 and @oil_etime is null)then
#						insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 0, '提醒', '您的油量少于', '10%', '请加油', null, null, 'GasLow');
#						update message_track_log set oil_send_status = 1 where obd_id = new.obd_id;
#					end if;
#	
#	#				将油耗信息放入车辆最新状态表
#					delete from vehicle_latest_status where vin = new.vin and item_key = 'oil_stat';
#					insert into vehicle_latest_status (vin, item_key, item_value, client_time) values (new.vin, 'oil_stat', @oil_stat, new.client_time);
#				end if;
#			end if;
#		end if;

#		message_id = 2d，私有协议
#		if(new.message_id = '2d')then
#			引擎on时，车门状态
#			if(new.message_content REGEXP 'accStatus=>3c' || new.message_content REGEXP 'accStatus=>31')then
#				车门状态为开
#				if(new.message_content REGEXP 'bonnetDoorStatus=>31' || new.message_content REGEXP 'driverDoorStatus=>31' || new.message_content REGEXP 'passengerDoorStatus=>31')then
#					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 1, '提醒', '您的爱车', '车门未关', '请检查', null, null, 'Door On');
#				end if;
#				后备箱为开
#				if(new.message_content REGEXP 'loadspaceDoorStatus=>31')then
#					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 1, '提醒', '您的爱车', '后备箱未关', '请检查', null, null, 'Trunk On');
#				end if;
#			end if;
#
#			引擎off时，车灯车窗状态
#			if(new.message_content REGEXP 'accStatus=>30')then
#				车门状态为开
#				if(new.message_content REGEXP 'bonnetDoorStatus=>31' || new.message_content REGEXP 'driverDoorStatus=>31' || new.message_content REGEXP 'passengerDoorStatus=>31')then
#					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 1, '提醒', '您的爱车', '车门未关', '请检查', null, null,'Door On');
#				end if;
#				后备箱为开
#				if(new.message_content REGEXP 'loadspaceDoorStatus=>31')then
#					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 1, '提醒', '您的爱车', '后备箱未关', '请检查', null, null, 'Trunk On');
#				end if;
#				车灯状态为开
#				if(new.message_content REGEXP 'leftDirectionLampInformation=>31' || new.message_content REGEXP 'rightDirectionLampInformation=>31' || new.message_content REGEXP 'fogLampInformation=>31' || new.message_content REGEXP 'highBeamLampInformation=>31' || new.message_content REGEXP 'lowBeamLampInformation=>31' || new.message_content REGEXP 'sideLampInformation=>31')then
#					insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 4, 1, '提醒', '您的爱车', '车灯未关', '请检查', null, null, 'Lamp On');
#				end if;
#			end if;

#			里程计算
#			set @content_rest = "";
#			set @total_km = "";
#			set @today_km = 0;
#
#			select substring(new.message_content, position('odometer=>' in new.message_content) + length('odometer=>')) into @content_rest;
#
#			select substring(@content_rest, 1, position(',' in @content_rest) - 1) into @total_km;

#			if(@total_km is not null and @total_km <> "")then			
#				获得今天的行驶里程
#				set @inttotalkm = 0;
#				set @inttoadykm = 0;
#				select total_km, today_km into @inttotalkm, @inttoadykm from vehicle_mileage where vin = new.vin and report_date = date(new.client_time);
#
#				如果今天的记录存在
#				if (@inttotalkm is not null and @inttotalkm > 0) then
#					if (@inttoadykm is null or @inttoadykm < 0) then
#						set @inttoadykm = 0;
#					end if;
#					算今天的行驶里程
#					set @inttodaykm_tmp = @total_km - @inttotalkm;
#					if (@inttodaykm_tmp > 0) then
#						set @inttoadykm = @inttoadykm + @inttodaykm_tmp;
#
#						delete from vehicle_mileage where vin = new.vin and report_date = date(new.client_time);
#						insert into vehicle_mileage (vin, report_date, total_km, today_km) values (new.vin, date(new.client_time), @total_km, @inttoadykm);
#					end if;
#				else 
#					当天没记录
#					delete from vehicle_mileage where vin = new.vin and report_date = date(new.client_time);
#					insert into vehicle_mileage (vin, report_date, total_km, today_km) values (new.vin, date(new.client_time), @total_km, 0);
#			end if;

#				算周里程
#				获得所在周的周一日期
#				set @dtweek_1stday = null;
#				set @week_km = 0;
#				select date_add(date(new.client_time), interval - weekday(date(new.client_time)) day) into @dtweek_1stday;
#				获得本周截止到上报天的里程
#				select sum(today_km) into @week_km
#				from vehicle_mileage
#				where vin = new.vin and report_date between @dtweek_1stday and date(new.client_time);
#
#				if (@week_km is null) then
#					set @week_km = 0;
#				end if;

#				获得所在月的第一天日期
#				set @dtmonth_1stday = null;
#				set @month_km = 0;
#				select date_sub(date(new.client_time),interval day(date(new.client_time))-1 day) into @dtmonth_1stday;
#				获得本月截止到上报天的里程
#				select sum(today_km) into @month_km
#				from vehicle_mileage
#				where vin = new.vin and report_date between @dtmonth_1stday and date(new.client_time);
#
#				if (@month_km is null) then
#					set @month_km = 0;
#				end if;

#				update vehicle_mileage
#					set week_km = @week_km,
#						month_km = @month_km
#				where vin = new.vin and report_date = date(new.client_time);
#		end if;
	end if;

end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `trig_vehicle_gps_log_ai`;
DELIMITER ;;
CREATE TRIGGER `trig_vehicle_gps_log_ai` AFTER INSERT ON `vehicle_gps_log` FOR EACH ROW begin 
	if (cast(new.longitude as signed) > 0 and cast(new.latitude as signed) >0 and (new.gps_stat = "A"))then	
#-----------------0829，多重电子围栏------------------------------------------- 
#得到用户设置的总围栏数 
		#gps时间加8小时=北京时间
		set @client_time=DATE_ADD(new.client_time,INTERVAL 8 hour);
		set @wnum = 0; 
		set @uid = 0; 
		SELECT uid into @uid FROM botaiapp.t_obd where obd_id=new.obd_id;
		#根据用户以及其他条件来判断目前生效的电子围栏数量
		select count(*) into @wnum 
		FROM botaiapp.t_address_book 
		where obd_id=new.obd_id 
		and	status=0 
		and floor(lat)<>floor(lng) 
		and wgs_lat>0 
		and in_open >= 0 
		and out_open >= 0 
		and user_id=@uid ; 
		
		set @i = 1; 
		while @i <= @wnum do 
			set @sname = ""; 
			set @strbaselng = ""; 
			set @strbaselat = ""; 
			set @intbaserange = 0; 
			set @booloutstat = 0; 
			set @boolinstat = 0; 
			set @in_stat = 0; 
			set @out_stat = 0; 
			set @id = 0; 
			set @tuid = 0; 
			set @address = "";
			#循环获取每个地址的开关状态，发送状态，初始坐标，设置距离 
			select cname,wgs_lat,wgs_lng ,in_open,out_open,range_num,in_stat,out_stat,id,user_id,address into @sname,@strbaselat,@strbaselng,@boolinstat,@booloutstat,@intbaserange,@in_stat,@out_stat,@id,@tuid,@address
			#select cname,lat,lng ,in_open,out_open,range_num,in_stat,out_stat,id,user_id into @sname,@strbaselat,@strbaselng,@boolinstat,@booloutstat,@intbaserange,@in_stat,@out_stat,@id,@tuid 
			from (select distinct if(name is null ,address,name) cname,id,range_num,wgs_lat,wgs_lng ,in_open,out_open,in_stat,out_stat,user_id,address,@rownum:=@rownum+1 AS rownum 
						FROM botaiapp.t_address_book a,(SELECT @rownum:=0) b 
						where obd_id = new.obd_id 
						and floor(lat)<>floor(lng) 
						and wgs_lat>0 
						and in_open >= 0 
						and out_open >= 0 
						and user_id=@uid 
						and	status = 0 
						ORDER BY id) t 
			where t.rownum = @i; 
			#计算距离 
			select ROUND((2*ASIN(SQRT(POW(SIN((RADIANS(new.latitude) -RADIANS(@strbaselat))/2),2) + COS(RADIANS(new.latitude))*COS(RADIANS(@strbaselat))*POW(SIN((RADIANS(new.longitude) -RADIANS(@strbaselng))/2),2)))) * 6378.137,2) into @strcurrrange; 
			#如果大于设置距离并且发送状态为未发送，那么进行生成消息并更新发送状态 
			if((@strcurrrange > @intbaserange) and (@out_stat = 0) and (@uid = @tuid))then 
			# 如果设置了打开驶出提醒，那么发送驶出报警 
				if (@booloutstat = 1) then 
					insert into accident_message (create_time,vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name, message_from, address) values (@client_time,new.vin, new.obd_id, 2, 1, '提醒', '您的爱车', concat('|离开|',@sname,'|',@intbaserange,'|'), '请检查', new.longitude, new.latitude, 'FenceOUT', @id, @address); 
					#insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 1, 2, '提醒', '您的爱车', concat('|驶出|',@sname), '请检查', new.longitude, new.latitude, 'FenceOUT'); 
				end if; 
			# 更新状态，已发驶出报警，不用再发 
				update botaiapp.t_address_book 
				set out_stat = 1 
				where obd_id = new.obd_id 
				and id = @id; 
			end if; 
			
			# 如果小于等于设置距离，并且驶入发送状态为未发送，驶出状态为发送，那么进行生成消息并更新发送状态 
			if((@strcurrrange <= @intbaserange) and (@in_stat = 0) and (@out_stat = 1) and (@uid = @tuid))then 
			# 如果设置了打开驶入提醒，那么发送驶入报警 
				if (@boolinstat = 1) then 
					insert into accident_message (create_time,vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name, message_from, address) values (@client_time,new.vin, new.obd_id, 2, 1, '提醒', '您的爱车', concat('|到达|',@sname,'|',@intbaserange,'|'), null, new.longitude, new.latitude, 'FenceIN', @id, @address); 
				#insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude, message_name) values (new.vin, new.obd_id, 1, 2, '提醒', '您的爱车', concat('|驶入|',@sname), null, new.longitude, new.latitude, 'FenceIN'); 
				end if; 
				
				# 更新状态表，已发驶入报警，初始化发送状态 
				update botaiapp.t_address_book 
				set in_stat = 0,out_stat = 0 
				where obd_id = new.obd_id 
				and id = @id; 
			end if; 
			
			#下一次循环条件 
			set @i = @i + 1; 
		end while; 
		
		# 更新车辆最后位置 
		replace into vehicle_latest_gps (vin, obd_id, longitude, latitude, speed, engine_speed, gps_stat, client_time) values (new.vin, new.obd_id, new.longitude, new.latitude, new.speed, new.engine_speed, new.gps_stat, new.client_time); 
	
	end if; 
	# 超速计算（evan) 
	#if (new.speed is not null and new.speed <> '' and new.speed>=125) then 
	#update vehicle_abnormal_speed_stat set over_speed_count = over_speed_count + 1 where vin = new.obd_id; 
	# insert into accident_message (vin, obd_id, message_type, message_level, title, message, message_value, alter_content, longitude, latitude) values (new.vin, new.obd_id, 2, 1, '警报', '您的爱车在', now(), '速度达到125KM/h', null, null); 
	#end if; 
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `trig_vehicle_latest_gps`;
DELIMITER ;;
CREATE TRIGGER `trig_vehicle_latest_gps` AFTER INSERT ON `vehicle_latest_gps` FOR EACH ROW begin

	replace into botaiapp.t_obd_latest_gps (vin, obd_id, longitude, latitude, speed, engine_speed, gps_stat, client_time) values (new.vin, new.obd_id, new.longitude, new.latitude, new.speed, new.engine_speed, new.gps_stat, new.client_time);

end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `trig_vehicle_latest_gps_update`;
DELIMITER ;;
CREATE TRIGGER `trig_vehicle_latest_gps_update` BEFORE UPDATE ON `vehicle_latest_gps` FOR EACH ROW begin

	replace into botaiapp.t_obd_latest_gps (vin, obd_id, longitude, latitude, speed, engine_speed, gps_stat, client_time) values (new.vin, new.obd_id, new.longitude, new.latitude, new.speed, new.engine_speed, new.gps_stat, new.client_time);

end
;;
DELIMITER ;
