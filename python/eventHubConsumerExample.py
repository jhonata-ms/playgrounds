from azure.eventhub import EventHubConsumerClient, EventHubSharedKeyCredential

eventhub_namespace = "nomeeventhubsnamespacehostname.servicebus.windows.net:9093"
eventhub_name = "nome.do.meu.eventhubsinstance"
consumer_group = "$Default"
shared_key_name = "SendAndReceiveOnly"
shared_key_value = "AbcDEFghiJ0="

def on_event(partition_context, event):
    print("Recebido evendo da partição: {}".format(partition_context.partition_id))
    print("Dados do evento: {}".format(event.body_as_str()))

credential = EventHubSharedKeyCredential(shared_key_name, shared_key_value)
consumer_client = EventHubConsumerClient(
    fully_qualified_namespace=eventhub_namespace,
    eventhub_name=eventhub_name,
    credential=credential,
    consumer_group=consumer_group
)

try:
    with consumer_client:
        consumer_client.receive(
            on_event=on_event,
            starting_position="-1"
        )
except:
    print("Recebimento de eventos interrompido.")
