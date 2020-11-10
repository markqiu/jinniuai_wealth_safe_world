from snbpy.common.domain.snb_config import SnbConfig
from snbpy.snb_api_client import SnbHttpClient


if __name__ == '__main__':
    config = SnbConfig()
    config.account = "DU2269542"
    config.key = '123456789'
    config.sign_type = 'None'
    config.snb_server ='sandbox.snbsecurities.com'
    config.snb_port = '443'
    config.timeout = 1000
    config.schema = 'https'

    client = SnbHttpClient(config)
    client.login()
    order_list_response = client.get_order_list()
    print(order_list_response.result_str)
    print(client.get_balance().result_str)
