DROP DATABASE IF EXISTS `django27`;
CREATE DATABASE `django27`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'mysql';
GRANT ALL PRIVILEGES ON django27.* TO 'kishita'@'localhost' IDENTIFIED BY 'yusuke0523'

WITH GRANT OPTION;
FLUSH PRIVILEGES;