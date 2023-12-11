-- database: wuliu.db


 -- SELECT * FROM bill_mount WHERE "任务单号"='TJ23073109995690'
  -- SELECT * FROM jdbill
 -- SELECT username,password,qx,memo FROM users

 SELECT * FROM jdbill join bill_mount WHERE jdbill.运输任务号 = bill_mount.任务单号