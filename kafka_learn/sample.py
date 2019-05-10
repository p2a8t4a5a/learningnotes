import pykafka
from pykafka import KafkaClient
from pykafka.common import OffsetType


client = KafkaClient(hosts="192.168.10.14:8092,192.168.10.15:8092,192.168.10.16:8092")
# topic = client.topics['test_account']
topic = client.topics['account']
consumer = topic.get_simple_consumer("test_account_group",
	auto_offset_reset = OffsetType.EARLIEST,
	reset_offset_on_start=False
)

for message in consumer:
    print message.value
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    # 	message.offset, message.key,
    #	message.value))
