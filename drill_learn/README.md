# start drill
bin/sqlline -u jdbc:drill:zk=local

# 文件系统查询
select sum(review_count) as totalreviews from dfs.`/<path-to-yelp-dataset>/yelp/yelp_academic_dataset_business.json`;



