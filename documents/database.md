数据库表满的原因

1. 没有设置成自动增加空间
SHOW GLOBAL VARIABLES LIKE 'innodb_data_file_path';
应该设置成为：innodb_data_file_path = ibdata1:10M:autoextend

  2. 磁盘的某个分区满了

  3. show table status;
有没有可能设置了一个max_row，导致达到上限
ALTER TABLE tbl_name MAX_ROWS=1000000000


