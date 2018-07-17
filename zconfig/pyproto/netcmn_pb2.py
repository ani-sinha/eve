# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: netcmn.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='netcmn.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cnetcmn.proto\"%\n\x07ipRange\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"7\n\x12ZnetStaticDNSEntry\x12\x10\n\x08HostName\x18\x01 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x02 \x03(\t\"\x89\x01\n\x06ipspec\x12\x17\n\x04\x64hcp\x18\x02 \x01(\x0e\x32\t.DHCPType\x12\x0e\n\x06subnet\x18\x03 \x01(\t\x12\x0f\n\x07gateway\x18\x05 \x01(\t\x12\x0e\n\x06\x64omain\x18\x06 \x01(\t\x12\x0b\n\x03ntp\x18\x07 \x01(\t\x12\x0b\n\x03\x64ns\x18\x08 \x03(\t\x12\x1b\n\tdhcpRange\x18\t \x01(\x0b\x32\x08.ipRange*M\n\x08\x44HCPType\x12\x0c\n\x08\x44HCPNoop\x10\x00\x12\n\n\x06Static\x10\x01\x12\x0f\n\x0bPassThrough\x10\x02\x12\n\n\x06Server\x10\x03\x12\n\n\x06\x43lient\x10\x04*A\n\x0bNetworkType\x12\x13\n\x0fNETWORKTYPENOOP\x10\x00\x12\x06\n\x02V4\x10\x04\x12\x06\n\x02V6\x10\x06\x12\r\n\tCryptoEID\x10\x0e\x42@\n\x1f\x63om.zededa.cloud.uservice.protoZ\x1dgithub.com/zededa/api/zconfigb\x06proto3')
)

_DHCPTYPE = _descriptor.EnumDescriptor(
  name='DHCPType',
  full_name='DHCPType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DHCPNoop', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Static', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PassThrough', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Server', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Client', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=252,
  serialized_end=329,
)
_sym_db.RegisterEnumDescriptor(_DHCPTYPE)

DHCPType = enum_type_wrapper.EnumTypeWrapper(_DHCPTYPE)
_NETWORKTYPE = _descriptor.EnumDescriptor(
  name='NetworkType',
  full_name='NetworkType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NETWORKTYPENOOP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V4', index=1, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V6', index=2, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CryptoEID', index=3, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=331,
  serialized_end=396,
)
_sym_db.RegisterEnumDescriptor(_NETWORKTYPE)

NetworkType = enum_type_wrapper.EnumTypeWrapper(_NETWORKTYPE)
DHCPNoop = 0
Static = 1
PassThrough = 2
Server = 3
Client = 4
NETWORKTYPENOOP = 0
V4 = 4
V6 = 6
CryptoEID = 14



_IPRANGE = _descriptor.Descriptor(
  name='ipRange',
  full_name='ipRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ipRange.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ipRange.end', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=53,
)


_ZNETSTATICDNSENTRY = _descriptor.Descriptor(
  name='ZnetStaticDNSEntry',
  full_name='ZnetStaticDNSEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='HostName', full_name='ZnetStaticDNSEntry.HostName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Address', full_name='ZnetStaticDNSEntry.Address', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=110,
)


_IPSPEC = _descriptor.Descriptor(
  name='ipspec',
  full_name='ipspec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dhcp', full_name='ipspec.dhcp', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subnet', full_name='ipspec.subnet', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='ipspec.gateway', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='ipspec.domain', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ntp', full_name='ipspec.ntp', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns', full_name='ipspec.dns', index=5,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dhcpRange', full_name='ipspec.dhcpRange', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=250,
)

_IPSPEC.fields_by_name['dhcp'].enum_type = _DHCPTYPE
_IPSPEC.fields_by_name['dhcpRange'].message_type = _IPRANGE
DESCRIPTOR.message_types_by_name['ipRange'] = _IPRANGE
DESCRIPTOR.message_types_by_name['ZnetStaticDNSEntry'] = _ZNETSTATICDNSENTRY
DESCRIPTOR.message_types_by_name['ipspec'] = _IPSPEC
DESCRIPTOR.enum_types_by_name['DHCPType'] = _DHCPTYPE
DESCRIPTOR.enum_types_by_name['NetworkType'] = _NETWORKTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ipRange = _reflection.GeneratedProtocolMessageType('ipRange', (_message.Message,), dict(
  DESCRIPTOR = _IPRANGE,
  __module__ = 'netcmn_pb2'
  # @@protoc_insertion_point(class_scope:ipRange)
  ))
_sym_db.RegisterMessage(ipRange)

ZnetStaticDNSEntry = _reflection.GeneratedProtocolMessageType('ZnetStaticDNSEntry', (_message.Message,), dict(
  DESCRIPTOR = _ZNETSTATICDNSENTRY,
  __module__ = 'netcmn_pb2'
  # @@protoc_insertion_point(class_scope:ZnetStaticDNSEntry)
  ))
_sym_db.RegisterMessage(ZnetStaticDNSEntry)

ipspec = _reflection.GeneratedProtocolMessageType('ipspec', (_message.Message,), dict(
  DESCRIPTOR = _IPSPEC,
  __module__ = 'netcmn_pb2'
  # @@protoc_insertion_point(class_scope:ipspec)
  ))
_sym_db.RegisterMessage(ipspec)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.zededa.cloud.uservice.protoZ\035github.com/zededa/api/zconfig'))
# @@protoc_insertion_point(module_scope)
