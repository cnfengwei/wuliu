-- database: wuliu.db
DELETE FROM jdbill
WHERE date("任务结束时间") > date('2023-08-03');