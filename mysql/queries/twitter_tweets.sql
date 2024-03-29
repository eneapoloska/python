CREATE DATABASE  IF NOT EXISTS `twitter` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `twitter`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: twitter
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tweets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tweet` varchar(140) DEFAULT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tweets_users1_idx` (`user_id`),
  CONSTRAINT `fk_tweets_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES (1,'There is power in understanding the journey of others to help create your own',1,'2002-02-01 00:00:01','2002-02-01 00:00:01'),(2,'Congrats Coach K! Amazing accomplishment #1KforCoachK #Duke',1,'2005-02-01 00:00:01','2005-02-01 00:00:01'),(3,'This is what happens when I pass too much! #ShoulderShock thank u all for ur thoughts and prayers #team @DrinkBODYARMOR @Lakers #oneluv',1,'2004-02-01 00:00:01','2004-02-01 00:00:01'),(4,'Feeling a mix of emotions I haven\'t felt in 18yrs of being a pro #journey #19th',1,'2012-02-01 00:00:01','2012-02-01 00:00:01'),(5,'Thank you everyone for the birthday wishes. I appreciate you all.',2,'2011-02-01 00:00:01','2011-02-01 00:00:01'),(6,'I\'d like to wish everyone a very Merry Christmas. 1 love to all \"Be Safe\"',2,'2009-02-01 00:00:01','2009-02-01 00:00:01'),(7,'Thanks to all who helped with the Christmas food baskets today. Your time is greatly appreciated. Love & Respect!! ',2,'2008-02-01 00:00:01','2008-02-01 00:00:01'),(8,'I took on the ALS Challenge from Monta Ellis. I challenge @coolkesh42 Jameer Nelson, Dionne Calhoun ... http://tmi.me/1eFAxT ',2,'2003-02-01 00:00:01','2003-02-01 00:00:01'),(9,'Well done lil bro, you deserve it!! @KingJames',3,'2006-02-01 00:00:01','2006-02-01 00:00:01'),(10,'For my basketball clinic with @manilacone 11/4/14, we still have a few slots left for the main game. See you all 11/5/14 Philippines',3,'2001-02-01 00:00:01','2001-02-01 00:00:01'),(11,'Always have a great time with my big little brother. ',4,'2011-02-01 00:00:01','2011-02-01 00:00:01'),(12,'Happy Labor Day..',4,'2014-02-01 00:00:01','2014-02-01 00:00:01');
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-06 17:24:45
