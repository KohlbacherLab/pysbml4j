# coding: utf-8

"""
    sbml4j API

    This is the api for the SBML4j Service   # noqa: E501

    OpenAPI spec version: 1.1.4
    Contact: thorsten.tiede@uni-tuebingen.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PathwayInventoryItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uuid': 'str',
        'name': 'str',
        'pathway_id': 'str',
        'organism_code': 'str',
        'number_of_nodes': 'int',
        'number_of_transitions': 'int',
        'number_of_reactions': 'int',
        'node_types': 'list[str]',
        'transition_types': 'list[str]',
        'compartments': 'list[str]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'uuid': 'UUID',
        'name': 'name',
        'pathway_id': 'pathwayId',
        'organism_code': 'organismCode',
        'number_of_nodes': 'numberOfNodes',
        'number_of_transitions': 'numberOfTransitions',
        'number_of_reactions': 'numberOfReactions',
        'node_types': 'nodeTypes',
        'transition_types': 'transitionTypes',
        'compartments': 'compartments',
        'links': 'links'
    }

    def __init__(self, uuid=None, name=None, pathway_id=None, organism_code=None, number_of_nodes=None, number_of_transitions=None, number_of_reactions=None, node_types=None, transition_types=None, compartments=None, links=None):  # noqa: E501
        """PathwayInventoryItem - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._name = None
        self._pathway_id = None
        self._organism_code = None
        self._number_of_nodes = None
        self._number_of_transitions = None
        self._number_of_reactions = None
        self._node_types = None
        self._transition_types = None
        self._compartments = None
        self._links = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if pathway_id is not None:
            self.pathway_id = pathway_id
        if organism_code is not None:
            self.organism_code = organism_code
        if number_of_nodes is not None:
            self.number_of_nodes = number_of_nodes
        if number_of_transitions is not None:
            self.number_of_transitions = number_of_transitions
        if number_of_reactions is not None:
            self.number_of_reactions = number_of_reactions
        if node_types is not None:
            self.node_types = node_types
        if transition_types is not None:
            self.transition_types = transition_types
        if compartments is not None:
            self.compartments = compartments
        if links is not None:
            self.links = links

    @property
    def uuid(self):
        """Gets the uuid of this PathwayInventoryItem.  # noqa: E501


        :return: The uuid of this PathwayInventoryItem.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PathwayInventoryItem.


        :param uuid: The uuid of this PathwayInventoryItem.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this PathwayInventoryItem.  # noqa: E501


        :return: The name of this PathwayInventoryItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PathwayInventoryItem.


        :param name: The name of this PathwayInventoryItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pathway_id(self):
        """Gets the pathway_id of this PathwayInventoryItem.  # noqa: E501


        :return: The pathway_id of this PathwayInventoryItem.  # noqa: E501
        :rtype: str
        """
        return self._pathway_id

    @pathway_id.setter
    def pathway_id(self, pathway_id):
        """Sets the pathway_id of this PathwayInventoryItem.


        :param pathway_id: The pathway_id of this PathwayInventoryItem.  # noqa: E501
        :type: str
        """

        self._pathway_id = pathway_id

    @property
    def organism_code(self):
        """Gets the organism_code of this PathwayInventoryItem.  # noqa: E501

        Three letter organism code this network belongs to  # noqa: E501

        :return: The organism_code of this PathwayInventoryItem.  # noqa: E501
        :rtype: str
        """
        return self._organism_code

    @organism_code.setter
    def organism_code(self, organism_code):
        """Sets the organism_code of this PathwayInventoryItem.

        Three letter organism code this network belongs to  # noqa: E501

        :param organism_code: The organism_code of this PathwayInventoryItem.  # noqa: E501
        :type: str
        """

        self._organism_code = organism_code

    @property
    def number_of_nodes(self):
        """Gets the number_of_nodes of this PathwayInventoryItem.  # noqa: E501


        :return: The number_of_nodes of this PathwayInventoryItem.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """Sets the number_of_nodes of this PathwayInventoryItem.


        :param number_of_nodes: The number_of_nodes of this PathwayInventoryItem.  # noqa: E501
        :type: int
        """

        self._number_of_nodes = number_of_nodes

    @property
    def number_of_transitions(self):
        """Gets the number_of_transitions of this PathwayInventoryItem.  # noqa: E501


        :return: The number_of_transitions of this PathwayInventoryItem.  # noqa: E501
        :rtype: int
        """
        return self._number_of_transitions

    @number_of_transitions.setter
    def number_of_transitions(self, number_of_transitions):
        """Sets the number_of_transitions of this PathwayInventoryItem.


        :param number_of_transitions: The number_of_transitions of this PathwayInventoryItem.  # noqa: E501
        :type: int
        """

        self._number_of_transitions = number_of_transitions

    @property
    def number_of_reactions(self):
        """Gets the number_of_reactions of this PathwayInventoryItem.  # noqa: E501


        :return: The number_of_reactions of this PathwayInventoryItem.  # noqa: E501
        :rtype: int
        """
        return self._number_of_reactions

    @number_of_reactions.setter
    def number_of_reactions(self, number_of_reactions):
        """Sets the number_of_reactions of this PathwayInventoryItem.


        :param number_of_reactions: The number_of_reactions of this PathwayInventoryItem.  # noqa: E501
        :type: int
        """

        self._number_of_reactions = number_of_reactions

    @property
    def node_types(self):
        """Gets the node_types of this PathwayInventoryItem.  # noqa: E501


        :return: The node_types of this PathwayInventoryItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_types

    @node_types.setter
    def node_types(self, node_types):
        """Sets the node_types of this PathwayInventoryItem.


        :param node_types: The node_types of this PathwayInventoryItem.  # noqa: E501
        :type: list[str]
        """

        self._node_types = node_types

    @property
    def transition_types(self):
        """Gets the transition_types of this PathwayInventoryItem.  # noqa: E501


        :return: The transition_types of this PathwayInventoryItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._transition_types

    @transition_types.setter
    def transition_types(self, transition_types):
        """Sets the transition_types of this PathwayInventoryItem.


        :param transition_types: The transition_types of this PathwayInventoryItem.  # noqa: E501
        :type: list[str]
        """

        self._transition_types = transition_types

    @property
    def compartments(self):
        """Gets the compartments of this PathwayInventoryItem.  # noqa: E501


        :return: The compartments of this PathwayInventoryItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._compartments

    @compartments.setter
    def compartments(self, compartments):
        """Sets the compartments of this PathwayInventoryItem.


        :param compartments: The compartments of this PathwayInventoryItem.  # noqa: E501
        :type: list[str]
        """

        self._compartments = compartments

    @property
    def links(self):
        """Gets the links of this PathwayInventoryItem.  # noqa: E501


        :return: The links of this PathwayInventoryItem.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PathwayInventoryItem.


        :param links: The links of this PathwayInventoryItem.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PathwayInventoryItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PathwayInventoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
