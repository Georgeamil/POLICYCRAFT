/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.5.8-log : Database - college_book
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`college_book` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `college_book`;

/*Table structure for table `academic_year` */

DROP TABLE IF EXISTS `academic_year`;

CREATE TABLE `academic_year` (
  `year_id` int(100) NOT NULL AUTO_INCREMENT,
  `academic_year` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`year_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `academic_year` */

insert  into `academic_year`(`year_id`,`academic_year`) values (1,'2016-2019'),(2,'2017-2019'),(3,'2018-2020'),(4,'2017-2020');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(100) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(100) DEFAULT NULL,
  `course_duration` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`course_name`,`course_duration`) values (1,'B. Sc ','3'),(2,'B.SC PYSICS VOCATIONAL','3'),(5,'B.SC PYSICS','3'),(6,'BCA','3');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exam_id` int(100) NOT NULL AUTO_INCREMENT,
  `course_id` varchar(100) DEFAULT NULL,
  `academic_year` varchar(100) DEFAULT NULL,
  `semester` varchar(100) DEFAULT NULL,
  `exam_name` varchar(100) DEFAULT NULL,
  `exam_detail` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`exam_id`,`course_id`,`academic_year`,`semester`,`exam_name`,`exam_detail`,`posted_date`) values (1,'6','4','1 SEMESTER','First Internal Examination','hsgfgsgaddfgasgf','2019-12-13'),(2,'6','3','2 SEMESTER','First internal Examination','hdjghjdsfhglhsdfg','2019-12-13'),(3,'6','3','1 SEMESTER','Second internal Examinations ','staring from the next week onwards','2019-12-13');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(100) NOT NULL AUTO_INCREMENT,
  `register_id` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `status` varchar(10) DEFAULT '0',
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`register_id`,`username`,`password`,`type`,`status`) values (1,'0','admin','admin123','admin','1'),(8,'7','megha@gmail.com','megha','teacher','1'),(10,'9','priya@gmail.com','priya','teacher','1');

/*Table structure for table `registration` */

DROP TABLE IF EXISTS `registration`;

CREATE TABLE `registration` (
  `register_id` int(100) NOT NULL AUTO_INCREMENT,
  `register_name` varchar(100) DEFAULT NULL,
  `register_mail` varchar(100) DEFAULT NULL,
  `register_phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`register_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `registration` */

insert  into `registration`(`register_id`,`register_name`,`register_mail`,`register_phone`) values (7,'Megha T B','megha@gmail.com','8028147457'),(9,'priya','priya@gmail.com','9908295472');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `stud_id` int(100) NOT NULL AUTO_INCREMENT,
  `stud_register_no` varchar(100) DEFAULT NULL,
  `stud_name` varchar(100) DEFAULT NULL,
  `stud_mail` varchar(100) DEFAULT NULL,
  `stud_phone` varchar(100) DEFAULT NULL,
  `parent_name` varchar(100) DEFAULT NULL,
  `parent_phone` varchar(100) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `academic_year` varchar(100) DEFAULT NULL,
  `semester` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`stud_id`,`stud_register_no`,`stud_name`,`stud_mail`,`stud_phone`,`parent_name`,`parent_phone`,`course`,`academic_year`,`semester`) values (1,'124364578596807','megha','megha@gmail.com','9789678568','babu','9879878164','2','2','2 SEMESTER'),(4,'100000000000001','priya','priya@gmail.com','9879869785','jose','8979879869','6','3','1 SEMESTER'),(5,'100000000000002','dilsha m deleep','dilsha@gmail.com','8697097609','deleep','7878678607','6','3','1 SEMESTER');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `sub_id` int(100) NOT NULL AUTO_INCREMENT,
  `course_id` varchar(50) DEFAULT NULL,
  `semester` varchar(100) DEFAULT NULL,
  `sub1` varchar(100) DEFAULT NULL,
  `sub2` varchar(100) DEFAULT NULL,
  `sub3` varchar(100) DEFAULT NULL,
  `sub4` varchar(100) DEFAULT NULL,
  `sub5` varchar(100) DEFAULT NULL,
  `sub6` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`sub_id`,`course_id`,`semester`,`sub1`,`sub2`,`sub3`,`sub4`,`sub5`,`sub6`) values (1,'6','1 SEMESTER','c','CPP','PMA','digital','stati','co');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
