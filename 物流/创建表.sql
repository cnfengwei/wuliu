-- database: wuliu.db
-- #在 BillMount 表中添加一个 insert_time 列，用于记录插入时间
-- ALTER TABLE bill_mount ADD insert_time DATETIME DEFAULT CURRENT_TIMESTAMP;
-- #在 JDBill 表中添加一个 insert_billmount 触发器，在插入新行时，自动插入一条 BillMount 表的行。
/*  CREATE TRIGGER insert_billmount
AFTER INSERT ON jdbill
FOR EACH ROW
BEGIN
  INSERT INTO bill_mount (
   任务单号,
   金额,
   审核,
   是否付款,
   备注,
   insert_time
  ) VALUES (
    NEW.运输任务号,
    0,
    0,
    0,
    null,
    CURRENT_TIMESTAMP
  );
END; 
DROP TRIGGER "main"."delete_billmount";
CREATE TRIGGER delete_billmount
AFTER DELETE ON jdbill
FOR EACH ROW
BEGIN
  UPDATE bill_mount
    SET deleted = TRUE
    WHERE 任务单号 = OLD.运输任务号;
END   
CREATE TABLE "jdbill" (
	"运输任务号"	TEXT NOT NULL UNIQUE,
	"任务开始时间"	TEXT NOT NULL,
	"任务结束时间"	TEXT NOT NULL,
	"三方单号"	TEXT NOT NULL,
	"始发网点"	TEXT NOT NULL,
	"目的网点"	TEXT NOT NULL,
	"车牌号"	TEXT NOT NULL,
	"计费车型"	TEXT NOT NULL,
	"三方司机姓名"	TEXT NOT NULL,
	"核实司机"	TEXT NOT NULL,
	PRIMARY KEY("运输任务号")
);
CREATE TABLE "bill_mount" (
	"任务单号"	TEXT NOT NULL UNIQUE,
	"金额"	NUMERIC DEFAULT 0,
	"审核"	BOOLEAN DEFAULT 0,
	"是否付款"	BOOLEAN DEFAULT 0,
	"备注"	INTEGER DEFAULT null,
	"deleted"	BOOLEAN DEFAULT FALSE,
	"insert_time"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("任务单号")
);