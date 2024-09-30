from netbox.plugins import PluginConfig

class NetBoxGetMacs(PluginConfig):
    name = 'netbox_get_macs'
    verbose_name = "NetBox Get Mac's"
    description = 'Получение Mac-адресов'
    version = '0.1'

config = NetBoxGetMacs