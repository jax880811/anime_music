DROP DATABASE IF EXISTS anime_song;

CREATE DATABASE anime_song CHARACTER SET big5;

USE anime_song;

DROP TABLE IF EXISTS anime_song;

CREATE TABLE `anime_song` (
  `歌曲名稱` varchar(45) NOT NULL,
  `作品名稱` varchar(45) DEFAULT NULL,
  `季度` int DEFAULT NULL,
  `播出年份` int DEFAULT NULL,
  `播出月份` int DEFAULT NULL,
  `演出團體或歌手` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`歌曲名稱`)
);


INSERT INTO `anime_song` (`歌曲名稱`, `作品名稱`, `季度`, `播出年份`, `播出月份`, `演出團體或歌手`)
VALUES
  ('Reweave', 'Re:從零開始的異世界生活', 3, 2024, 10, '鈴木このみ'),
  ('PEACEKEEPER', '關於我轉生變成史萊姆這檔事', 3, 2024, 4, 'STEREO DIVE FOUNDATION');
