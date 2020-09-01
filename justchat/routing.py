from channels.routing import ProtocolTypeRouter


application = ProtocolTypeRouter({})

routing_websocket = [
    route(“websocket.connect”, websocket_connect),
    route(“websocket.receive”, websocket_receive),
    route(“websocket.disconnect”, websocket_disconnect),
]
routing_chat = [
    route(“chat.receive”, join_chat, command=”^join$”),
    route(“chat.receive”, leave_chat, command=”^leave$”),
    route(“chat.receive”, send_chat, command=”^send$”),
]