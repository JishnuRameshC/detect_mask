/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.6.17 : Database - facemaskdetection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`facemaskdetection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `facemaskdetection`;

/*Table structure for table `aadhar` */

DROP TABLE IF EXISTS `aadhar`;

CREATE TABLE `aadhar` (
  `aadharid` int(11) NOT NULL AUTO_INCREMENT,
  `aadhar_number` bigint(20) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`aadharid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `aadhar` */

insert  into `aadhar`(`aadharid`,`aadhar_number`,`userid`) values 
(1,0,0),
(2,777777777,6);

/*Table structure for table `assign_fine` */

DROP TABLE IF EXISTS `assign_fine`;

CREATE TABLE `assign_fine` (
  `afineid` int(11) NOT NULL AUTO_INCREMENT,
  `fineid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `datetime` date DEFAULT NULL,
  PRIMARY KEY (`afineid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `assign_fine` */

insert  into `assign_fine`(`afineid`,`fineid`,`userid`,`datetime`) values 
(1,2,6,'2021-03-16'),
(2,2,1,'2021-04-07'),
(3,2,2,'2021-04-07'),
(4,2,6,'2021-04-07');

/*Table structure for table `camera` */

DROP TABLE IF EXISTS `camera`;

CREATE TABLE `camera` (
  `cameraid` int(11) NOT NULL AUTO_INCREMENT,
  `serial` bigint(20) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `loc` varchar(200) DEFAULT NULL,
  `lat` varchar(20) DEFAULT NULL,
  `lon` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cameraid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `camera` */

insert  into `camera`(`cameraid`,`serial`,`model`,`loc`,`lat`,`lon`) values 
(2,102,'XHKG','kannur','1234321.11','6755434.98');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaintid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `complaint date` varchar(20) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `replydate` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`complaintid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaintid`,`userid`,`complaint`,`complaint date`,`reply`,`replydate`) values 
(1,1,'bad','13/12/1545','sad','2021-03-03'),
(2,6,'tttttttttttttttttt','2021-03-09','pending',''),
(3,6,'ooooooooo','2021-03-12','pending','');

/*Table structure for table `facemask` */

DROP TABLE IF EXISTS `facemask`;

CREATE TABLE `facemask` (
  `facemaskid` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(500) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `trafficpoliceid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`facemaskid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `facemask` */

insert  into `facemask`(`facemaskid`,`photo`,`date`,`time`,`status`,`trafficpoliceid`,`userid`) values 
(1,NULL,'2020-09-08','22:00:00','generated',3,6),
(2,NULL,'2020-09-08','22:00:00','pending',3,6);

/*Table structure for table `fine` */

DROP TABLE IF EXISTS `fine`;

CREATE TABLE `fine` (
  `fineid` int(11) NOT NULL AUTO_INCREMENT,
  `details` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `fine` int(11) DEFAULT NULL,
  PRIMARY KEY (`fineid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fine` */

insert  into `fine`(`fineid`,`details`,`description`,`fine`) values 
(2,'qq','weq',1200);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`type`) values 
(1,'a','12','admin'),
(3,'tp','1472','tp'),
(5,NULL,NULL,NULL),
(6,'u','11','user'),
(7,'ggg','11','user'),
(8,'ggg','1111','user'),
(9,'sss','aa','user');

/*Table structure for table `trafficpolice` */

DROP TABLE IF EXISTS `trafficpolice`;

CREATE TABLE `trafficpolice` (
  `trafficid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `qualification` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`trafficid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `trafficpolice` */

insert  into `trafficpolice`(`trafficid`,`name`,`phone`,`email`,`gender`,`qualification`) values 
(3,'muhsin',12345678,'nazirjr111@gmail.com','male','refrttrthghgh\r\n        \r\n        ');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`userid`,`uname`,`phone`,`email`,`gender`,`photo`) values 
(1,'ffdfdf',0,'vcvcvcv','male','b.jpg'),
(2,'RER',456789,'hghghghgh','male','b.jpg'),
(6,'yyyyy',888888,'hhh@gmail.com','male','b.jpg');

/*Table structure for table `violation` */

DROP TABLE IF EXISTS `violation`;

CREATE TABLE `violation` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `violation` varchar(50) DEFAULT NULL,
  `penalty` int(50) DEFAULT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `violation` */

insert  into `violation`(`vid`,`violation`,`penalty`) values 
(1,'d',12222);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
