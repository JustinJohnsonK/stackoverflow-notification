import pgi
pgi.require_version('Notify', '0.7')
from pgi.repository import Notify
Notify.init("Test Notifier")

class DisplayNotification(object):

    def __init__(self, reputation):
        self.rep = reputation
        notification = Notify.Notification.new(
            "Your Reputation \n",
            self.rep + "\n",
            "Bronze",
        )
        notification.show()