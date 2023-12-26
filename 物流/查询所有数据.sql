-- database: wuliu.db


  -- SELECT * FROM bill_mount WHERE "任务单号"='TJ23080310241108'
   -- SELECT * FROM jdbill where "运输任务号" = 'TJ23080310241108'
 -- SELECT username,password,qx,memo FROM users

 -- SELECT "运输任务号","核实司机","车牌号","金额","审核","是否付款","开始时间","三方单号","三方司机","备注" FROM bill_view where 核实司机="张占山"
-- SELECT '运输任务号','核实司机','车牌号','金额','审核','是否付款','开始时间','三方单号','三方司机','备注' FROM bill_view
-- SELECT "运输任务号", "核实司机", "三方司机姓名" ,"车牌号", "始发网点","目的网点", "金额", "任务开始时间",
 -- "任务结束时间","三方单号", "备注" FROM bill_view where  "任务开始时间" >= '2023-08-05' and "任务开始时间" <='2023-08-11'

 SELECT "运输任务号", "核实司机", "三方司机姓名" ,"车牌号","始发网点","目的网点", "金额", "任务开始时间", "任务结束时间",
 "三方单号", "备注" FROM bill_view where   date("任务开始时间") >= '2023-08-01' AND  date("任务开始时间") <= '2023-08-03'