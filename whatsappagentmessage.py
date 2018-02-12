'''
Created on Feb 11, 2018

@author: ctaunk
'''


class WhatsAppAgentMessage(object):

    def __init__(self, chatId=None, chatName=None, senderId=None, senderName=None, msgType=None, msgData=None, msgTime=None):
        self.chatId = chatId
        self.chatName = chatName
        self.senderId = senderId
        self.senderName = senderName
        self.msgType = msgType
        self.msgData = msgData
        self.msgTime = msgTime
        
    def get_chat_id(self):
        return self.__chatId

    def get_chat_name(self):
        return self.__chatName

    def get_sender_id(self):
        return self.__senderId

    def get_sender_name(self):
        return self.__senderName

    def get_msg_type(self):
        return self.__msgType

    def get_msg_data(self):
        return self.__msgData

    def get_msg_time(self):
        return self.__msgTime

    def set_chat_id(self, value):
        self.__chatId = value

    def set_chat_name(self, value):
        self.__chatName = value

    def set_sender_id(self, value):
        self.__senderId = value

    def set_sender_name(self, value):
        self.__senderName = value

    def set_msg_type(self, value):
        self.__msgType = value

    def set_msg_data(self, value):
        self.__msgData = value

    def set_msg_time(self, value):
        self.__msgTime = value

    def del_chat_id(self):
        del self.__chatId

    def del_chat_name(self):
        del self.__chatName

    def del_sender_id(self):
        del self.__senderId

    def del_sender_name(self):
        del self.__senderName

    def del_msg_type(self):
        del self.__msgType

    def del_msg_data(self):
        del self.__msgData

    def del_msg_time(self):
        del self.__msgTime
    
    chatId = property(get_chat_id, set_chat_id, del_chat_id, "chatId's docstring")
    chatName = property(get_chat_name, set_chat_name, del_chat_name, "chatName's docstring")
    senderId = property(get_sender_id, set_sender_id, del_sender_id, "senderId's docstring")
    senderName = property(get_sender_name, set_sender_name, del_sender_name, "senderName's docstring")
    msgType = property(get_msg_type, set_msg_type, del_msg_type, "msgType's docstring")
    msgData = property(get_msg_data, set_msg_data, del_msg_data, "msgData's docstring")
    msgTime = property(get_msg_time, set_msg_time, del_msg_time, "msgTime's docstring")

    def csv_format(self):
        row = self.__chatId
        row = row + "," + self.__chatName
        row = row + "," + self.__senderId
        row = row + "," + self.__senderName
        row = row + "," + self.__msgTime
        row = row + "," + self.__msgType
        row = row + "," + self.__msgData
        row = row + "," + self.__chatName
        return row
    
    def readable_format(self):
        text = '<{time}> from <{sender}> message "{msg}"'.format(
            time=self.msgTime, 
            sender=self.senderName, 
            msg=self.msgData)
        return text
