-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 10, 2021 at 09:09 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `policy_craft`
--

-- --------------------------------------------------------

--
-- Table structure for table `amount`
--

CREATE TABLE IF NOT EXISTS `amount` (
  `amt_id` int(100) NOT NULL AUTO_INCREMENT,
  `amount` varchar(100) DEFAULT NULL,
  `com_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`amt_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `amount`
--

INSERT INTO `amount` (`amt_id`, `amount`, `com_id`) VALUES
(4, '100000', '7'),
(5, '200000', '7'),
(6, '350000', '7'),
(7, '1000000', '6'),
(8, '100000', '10'),
(9, '300000', '10'),
(10, '450000', '10'),
(11, '3000', '10');

-- --------------------------------------------------------

--
-- Table structure for table `applications`
--

CREATE TABLE IF NOT EXISTS `applications` (
  `apl_id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `p_id` varchar(100) DEFAULT NULL,
  `com_id` varchar(100) DEFAULT NULL,
  `cat_id` varchar(100) DEFAULT NULL,
  `u_id` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`apl_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `applications`
--

INSERT INTO `applications` (`apl_id`, `name`, `gender`, `age`, `dob`, `address`, `phone`, `email`, `p_id`, `com_id`, `cat_id`, `u_id`, `status`) VALUES
(1, 'Aneeja', 'female', '23', '2019-12-11', 'aaaaaa', '888797898', 'aneeja@gmail.com', '4', '6', '8', '2', 'Completed'),
(2, 'sam', 'male', '56', '2019-12-11', 'aaaa', '8989898989', 'sam@gmail.com', '4', '6', '8', '2', 'Rejected'),
(3, 'aaa', 'female', '12', '2019-12-06', 'aaa', '780987909', 'a@g.n', '4', '6', '8', '2', 'Rejected'),
(4, 'neena', 'female', '33', '2019-12-11', 'AADSFS', '8888888888', 'A@H.M', '4', '6', '8', '2', 'Rejected'),
(5, 'meenu', 'female', '22', '2019-12-01', 'aluva', '8888888888', 'meenu@gmail.com', '4', '6', '8', '2', 'Approved'),
(6, 'nisha', 'female', '20', '2019-12-01', 'aaaa', '9999999999', 'nisha@gmail.com', '4', '6', '8', '2', 'Rejected'),
(8, 'q', 'female', '22', '2019-12-25', 'aSQWA', '9898989896', 'A@G.M', '6', '6', '6', '2', 'Applied'),
(9, 'sajitha babu', 'female', '23', '1989-12-31', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'meghatb@gmail.com', '4', '6', '5', '2', 'Rejected'),
(10, 'dilsha', 'female', '23', '1995-12-04', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'meghatb@gmail.com', '4', '6', '5', '3', 'Approved'),
(11, 'Meritta', 'female', '23', '1995-01-01', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'aneeja@gmail.com', '9', '10', '7', '3', 'Completed');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
  `cat_id` int(100) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cat_id`, `cat_name`) VALUES
(5, 'Life Insurance'),
(6, 'Vehicle Insurance'),
(7, 'Health Insurance'),
(9, 'Cyber Insurance');

-- --------------------------------------------------------

--
-- Table structure for table `company_register`
--

CREATE TABLE IF NOT EXISTS `company_register` (
  `c_id` int(100) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(100) DEFAULT NULL,
  `c_reg_no` varchar(100) DEFAULT NULL,
  `c_email` varchar(100) DEFAULT NULL,
  `c_address` varchar(200) DEFAULT NULL,
  `c_phone` varchar(100) DEFAULT NULL,
  `c_doc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `company_register`
--

INSERT INTO `company_register` (`c_id`, `c_name`, `c_reg_no`, `c_email`, `c_address`, `c_phone`, `c_doc`) VALUES
(6, 'LIC', '788900', 'lic@gmail.com', 'trivandrum', '89989020', 'static/Media/g2.jpg'),
(8, 'lcc', '9999999999999999', 'google@email.com', 'scfadsfv', '9874563210', 'static/Media/typeimage.jpg'),
(10, 'bajaj', '8990889990777878', 'bajaj@gmail.com', 'aluva', '8909787786', 'static/Media/PetVet.docx');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `log_id` int(100) NOT NULL AUTO_INCREMENT,
  `reg_id` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT '0',
  `type` varchar(100) DEFAULT NULL,
  `count` int(11) NOT NULL,
  `bstatus` varchar(50) NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`log_id`, `reg_id`, `email`, `password`, `status`, `type`, `count`, `bstatus`) VALUES
(1, '0', 'admin', 'admin123', '1', 'admin', 0, ''),
(5, '6', 'lic@gmail.com', 'lic', '1', 'company', 0, ''),
(8, '8', 'google@email.com', '123456789', '1', 'company', 0, ''),
(10, '2', 'priya@gmail.com', 'priya', '1', 'user', 0, ''),
(11, '10', 'bajaj@gmail.com', 'bajaj', '1', 'company', 0, ''),
(12, '3', 'aneeja@gmail.com', 'aneeja', '1', 'user', 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE IF NOT EXISTS `payment` (
  `pay_id` int(100) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(100) DEFAULT NULL,
  `c_id` varchar(100) DEFAULT NULL,
  `policy_id` varchar(100) DEFAULT NULL,
  `cardno` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `appl_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pay_id`, `u_id`, `c_id`, `policy_id`, `cardno`, `date`, `amount`, `appl_id`) VALUES
(1, '2', '6', '4', '1123214234', '2019-12-23', '1000000', '1'),
(2, '2', '6', '4', '1234566778', '2020-01-06', '100', '3'),
(3, '2', '6', '4', '123445523444', '2020-01-06', '100', '3'),
(4, '3', '10', '9', '1111652461475174', '2020-01-06', '1000', '11'),
(5, '3', '10', '9', '2222222222222222', '2020-01-06', '1000', '11'),
(6, '3', '10', '9', '123445523444', '2020-01-06', '1000', '11'),
(7, '3', '6', '4', '123445523444', '2020-01-06', '100', '10'),
(8, '3', '6', '4', '123445523444', '2020-01-06', '100', '10'),
(9, '3', '6', '4', '123445523444', '2020-01-06', '100', '10');

-- --------------------------------------------------------

--
-- Table structure for table `policy`
--

CREATE TABLE IF NOT EXISTS `policy` (
  `p_id` int(100) NOT NULL AUTO_INCREMENT,
  `p_name` varchar(100) DEFAULT NULL,
  `cat_id` varchar(100) DEFAULT NULL,
  `amount_id` varchar(100) DEFAULT NULL,
  `premium_id` varchar(100) DEFAULT NULL,
  `p_duration` varchar(100) DEFAULT NULL,
  `p_description` varchar(100) DEFAULT NULL,
  `p_document` varchar(100) DEFAULT NULL,
  `com_id` varchar(100) DEFAULT NULL,
  `payment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `policy`
--

INSERT INTO `policy` (`p_id`, `p_name`, `cat_id`, `amount_id`, `premium_id`, `p_duration`, `p_description`, `p_document`, `com_id`, `payment`) VALUES
(4, 'life reksha', '5', '7', '8', '3', 'nice policy', 'static/Media/Permission%20Code.txt', '6', '100'),
(5, 'Jeevan Reksha POlicy', '5', '10', '13', '36', 'new Policy', 'static/Media/dbpage.docx', '10', '100'),
(6, 'lvehicle support', '6', '7', '8', '32', 'aaaaa', 'static/Media/Motor%20Vehicle%20Insurance%20Application%20.pdf', '6', '2000'),
(7, 'aaaaaaaaa', '5', '7', '8', '1000', 'aaaaaaaaaaaaaaaaaaaaa', 'static/Media/Motor%20Vehicle%20Insurance%20Application%20_Ko303Rl.pdf', '6', '100'),
(8, 'mmmmmm', '5', '7', '8', '22', 'qasdgdfhg', 'static/Media/Application%20form%20for%20Health%20Insurance.pdf', '6', '1500'),
(9, 'Old_Health', '7', '11', '12', '12', 'New Policy for old peoples', 'static/Media/jsooon.txt', '10', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `premium`
--

CREATE TABLE IF NOT EXISTS `premium` (
  `pre_id` int(100) NOT NULL AUTO_INCREMENT,
  `pre_type` varchar(100) DEFAULT NULL,
  `com_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pre_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `premium`
--

INSERT INTO `premium` (`pre_id`, `pre_type`, `com_id`) VALUES
(1, 'Lump Sum', '7'),
(2, 'Monthly', '7'),
(3, 'Quarterly', '7'),
(4, 'Semi-Annually', '7'),
(5, 'Annually', '7'),
(8, 'Monthly', '6'),
(9, 'Yearly', '6'),
(10, 'Lumb Sum', '6'),
(11, 'Lumb Sum', '10'),
(12, 'Monthly', '10'),
(13, 'Quarterly', '10'),
(14, 'Yearly', '10');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE IF NOT EXISTS `rating` (
  `rate_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) DEFAULT NULL,
  `com_id` varchar(100) DEFAULT NULL,
  `p_id` varchar(100) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`rate_id`, `user_id`, `com_id`, `p_id`, `rating`, `posted_date`, `feedback`) VALUES
(2, '2', '6', '4', '4', '2020-01-05', 'nice policy'),
(3, '3', '10', '9', '4.5', '2020-01-06', 'very nice app');

-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE IF NOT EXISTS `user_register` (
  `u_id` int(100) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(100) DEFAULT NULL,
  `u_email` varchar(100) DEFAULT NULL,
  `u_address` varchar(100) DEFAULT NULL,
  `u_phone` varchar(100) DEFAULT NULL,
  `u_gender` varchar(100) DEFAULT NULL,
  `u_dob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_register`
--

INSERT INTO `user_register` (`u_id`, `u_name`, `u_email`, `u_address`, `u_phone`, `u_gender`, `u_dob`) VALUES
(2, 'priya jose', 'priya@gmail.com', 'kalapparambath', '8891878989', 'female', '2019-12-18'),
(3, 'aneeja joy', 'aneeja@gmail.com', 'fsfsggf', '8089186044', 'female', '1995-12-04');
