-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recog
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `registro`
--

DROP TABLE IF EXISTS `registro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `fecha` varchar(45) DEFAULT NULL,
  `camara` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro`
--

LOCK TABLES `registro` WRITE;
/*!40000 ALTER TABLE `registro` DISABLE KEYS */;
INSERT INTO `registro` VALUES (1,'Desconocido','2024-11-24 16:05:23','1'),(2,'Desconocido','2024-11-24 16:05:29','1'),(3,'Desconocido','2024-11-24 16:05:31','1'),(4,'Desconocido','2024-11-24 16:06:17','1'),(5,'Desconocido','2024-11-24 16:06:27','1'),(6,'Desconocido','2024-11-24 16:06:41','1'),(7,'Desconocido','2024-11-24 16:06:42','1'),(8,'Desconocido','2024-11-24 16:06:43','1'),(9,'Desconocido','2024-11-24 16:06:44','1'),(10,'Desconocido','2024-11-24 16:08:08','1'),(11,'Desconocido','2024-11-24 16:08:10','1'),(12,'Desconocido','2024-11-24 16:08:11','1'),(13,'Desconocido','2024-11-24 16:08:12','1'),(14,'Desconocido','2024-11-24 16:08:13','1'),(15,'Desconocido','2024-11-24 16:08:18','1'),(16,'Desconocido','2024-11-24 16:08:24','1'),(17,'Desconocido','2024-11-24 16:08:26','1'),(18,'Desconocido','2024-11-24 16:08:27','1'),(19,'Desconocido','2024-11-24 16:08:28','1'),(20,'Desconocido','2024-11-24 16:08:29','1'),(21,'Desconocido','2024-11-24 16:10:19','1'),(22,'Desconocido','2024-11-24 16:10:21','1'),(23,'Desconocido','2024-11-24 16:10:22','1'),(24,'Desconocido','2024-11-24 16:10:23','1'),(25,'Desconocido','2024-11-24 16:10:24','1'),(26,'Desconocido','2024-11-24 16:10:25','2'),(27,'Desconocido','2024-11-24 16:10:26','2'),(28,'Desconocido','2024-11-24 16:10:35','1'),(29,'Desconocido','2024-11-24 16:10:36','1'),(30,'Desconocido','2024-11-24 16:10:39','1'),(31,'Desconocido','2024-11-24 16:10:40','1'),(32,'Desconocido','2024-11-24 16:10:40','1'),(33,'Desconocido','2024-11-24 16:10:41','1'),(34,'Desconocido','2024-11-24 16:10:42','2'),(35,'Desconocido','2024-11-24 16:10:47','1'),(36,'Desconocido','2024-11-24 16:10:49','2'),(37,'Desconocido','2024-11-24 16:10:51','1'),(38,'Desconocido','2024-11-24 16:10:52','1'),(39,'Desconocido','2024-11-24 17:03:48','1'),(40,'Desconocido','2024-11-24 17:03:53','1'),(41,'Desconocido','2024-11-24 17:04:01','1'),(42,'Desconocido','2024-11-24 17:04:02','1'),(43,'Desconocido','2024-11-24 17:04:12','1'),(44,'Desconocido','2024-11-24 17:04:17','2'),(45,'Desconocido','2024-11-24 17:04:20','2'),(46,'Desconocido','2024-11-24 17:04:24','2'),(47,'Desconocido','2024-11-24 17:04:25','2'),(48,'Desconocido','2024-11-24 17:04:26','2'),(49,'Desconocido','2024-11-24 17:04:27','2');
/*!40000 ALTER TABLE `registro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-24 17:06:51
