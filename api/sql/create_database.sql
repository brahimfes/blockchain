CREATE DATABASE sih;

use sih;

CREATE TABLE `sih`.`patient` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `pid` VARCHAR(45) NOT NULL,
    `nom` VARCHAR(45) NOT NULL,
    `prenom` VARCHAR(45) NOT NULL,
    `date_naissance` VARCHAR(45) NOT NULL,
    `sexe` CHAR(1) NOT NULL,
    `adresse` VARCHAR(200) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `sih`.`obx` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `pid` VARCHAR(45) NOT NULL,
    `set_id` VARCHAR(45) NOT NULL,
    `value` VARCHAR(45) NOT NULL,
    `units` VARCHAR(45) NOT NULL,
    `references_range` CHAR(1) NOT NULL,
    `result` VARCHAR(45) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `sih`.`valise` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `checkout` VARCHAR(45) NOT NULL,
    `date` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `sih`.`blockchain` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `version` VARCHAR(45) NOT NULL,
    `date` TIMESTAMP NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `sih`.`rapport` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `content` TEXT NOT NULL,
    `pid` VARCHAR(45) NOT NULL,
    `date` TIMESTAMP NOT NULL,
    `user` BIGINT NOT NULL,
    PRIMARY KEY (`id`)
);


