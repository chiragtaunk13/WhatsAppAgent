'''
Created on Feb 11, 2018

@author: ctaunk
'''
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from whatsappagentmessage import WhatsAppAgentMessage
from whatsappagentconstants import WhatsAppAgentConstants

import time
import logging.config
logger = logging.getLogger(__name__)
logging.config.fileConfig(WhatsAppAgentConstants.LOG_CONF_FILE, disable_existing_loggers=False)

class WhatsAppAgent(object):

    def __init__(self):
        self.driver = WhatsAPIDriver(client=WhatsAppAgentConstants.BROWSER)
        logger.info("Waiting for successful QR Code scan...")
        self.driver.wait_for_login()
        logger.info("Logged in!")

    def get_all_chats(self):
        return self.driver.get_all_chats()
    
    def get_all_msgs_in_chat(self, chat=None):
        if chat is None:
            return []
        return self.driver.get_all_messages_in_chat(chat)
    
    def get_msg_text(self, message=None):
        if message is None:
            return ""
        return message.safe_content
    
    def get_unread_msgs(self):
        for contact in self.driver.get_unread():
            for message in contact.messages:
                if isinstance(message, Message):
                    whatsAppMsg = WhatsAppAgentMessage(
                        chatId=contact.chat.id,
                        chatName=contact.chat.name,
                        senderId="",
                        senderName=message.sender.get_safe_name(),
                        msgType="",
                        msgData=message.safe_content,
                        msgTime=message.timestamp)
                    
                    logger.debug("New message: %s", whatsAppMsg.readable_format())
    def run(self):
        while True:
            time.sleep(WhatsAppAgentConstants.NEW_MSG_POLL)
            self.get_unread_msgs()


            
myWhatsAppAgent = WhatsAppAgent()
myWhatsAppAgent.run()
