/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80040 (8.0.40)
 Source Host           : 127.0.0.1:3306
 Source Schema         : fortune

 Target Server Type    : MySQL
 Target Server Version : 80040 (8.0.40)
 File Encoding         : 65001

 Date: 12/02/2025 00:29:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bazi_analysis
-- ----------------------------
DROP TABLE IF EXISTS `bazi_analysis`;
CREATE TABLE `bazi_analysis`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `bazi` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `createtime` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `gender` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
