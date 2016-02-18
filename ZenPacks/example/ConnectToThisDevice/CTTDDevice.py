from . import schema


class CTTDDevice(schema.CTTDDevice):
    def sshLink(self):
        return "https://{}:8443".format(self.manageIp)
