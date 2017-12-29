# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TwinContent(Model):
    """TwinContent.

    :param target_property_path:
    :type target_property_path: str
    :param target_content:
    :type target_content: dict
    """

    _attribute_map = {
        'target_property_path': {'key': 'TargetPropertyPath', 'type': 'str'},
        'content': {'key': 'TargetContent', 'type': '{object}'},
    }

    def __init__(self, target_property_path=None, target_content=None):
        self.target_property_path = target_property_path
        self.target_content = target_content