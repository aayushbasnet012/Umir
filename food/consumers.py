import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

from food.models import MenuItems, Orders, Table
class OrderConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        print(text_data_json)
        print(type(text_data_json))
        # print(Table.objects.get(text_data_json['table_id']))
        # chreate new order object
        order = Orders(
            id=1,
            table_id = Table.objects.get(GUID=text_data_json['table_id']),
            item_id = MenuItems.objects.get(id=text_data_json['id']),
            quantity = text_data_json['quantity'],
            order_state = "ordered"
        )
        order.save()

        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type':'chat_message',   
                    
        #     }
        # )

    # def chat_message(self, event):
    #     message = event['message']

    #     self.send(text_data=json.dumps({
    #         'type':'chat',
    #         'message':message
    #     }))