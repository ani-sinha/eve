# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='register.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('Z&github.com/lf-edge/eve/api/go/register'),
  serialized_pb=_b('\n\x0eregister.proto\"1\n\rZRegisterResp\x12 \n\x06result\x18\x02 \x01(\x0e\x32\x10.ZRegisterResult\"C\n\x0cZRegisterMsg\x12\x12\n\nonBoardKey\x18\x01 \x01(\t\x12\x0f\n\x07pemCert\x18\x02 \x01(\x0c\x12\x0e\n\x06serial\x18\x03 \x01(\t*z\n\x0fZRegisterResult\x12\x0c\n\x08ZRegNone\x10\x00\x12\x0f\n\x0bZRegSuccess\x10\x01\x12\x11\n\rZRegNotActive\x10\x02\x12\x13\n\x0fZRegAlreadyDone\x10\x03\x12\x10\n\x0cZRegDeviceNA\x10\x04\x12\x0e\n\nZRegFailed\x10\x05\x42(Z&github.com/lf-edge/eve/api/go/registerb\x06proto3')
)

_ZREGISTERRESULT = _descriptor.EnumDescriptor(
  name='ZRegisterResult',
  full_name='ZRegisterResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZRegNone', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZRegSuccess', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZRegNotActive', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZRegAlreadyDone', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZRegDeviceNA', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZRegFailed', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=260,
)
_sym_db.RegisterEnumDescriptor(_ZREGISTERRESULT)

ZRegisterResult = enum_type_wrapper.EnumTypeWrapper(_ZREGISTERRESULT)
ZRegNone = 0
ZRegSuccess = 1
ZRegNotActive = 2
ZRegAlreadyDone = 3
ZRegDeviceNA = 4
ZRegFailed = 5



_ZREGISTERRESP = _descriptor.Descriptor(
  name='ZRegisterResp',
  full_name='ZRegisterResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ZRegisterResp.result', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=67,
)


_ZREGISTERMSG = _descriptor.Descriptor(
  name='ZRegisterMsg',
  full_name='ZRegisterMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='onBoardKey', full_name='ZRegisterMsg.onBoardKey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pemCert', full_name='ZRegisterMsg.pemCert', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial', full_name='ZRegisterMsg.serial', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=136,
)

_ZREGISTERRESP.fields_by_name['result'].enum_type = _ZREGISTERRESULT
DESCRIPTOR.message_types_by_name['ZRegisterResp'] = _ZREGISTERRESP
DESCRIPTOR.message_types_by_name['ZRegisterMsg'] = _ZREGISTERMSG
DESCRIPTOR.enum_types_by_name['ZRegisterResult'] = _ZREGISTERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZRegisterResp = _reflection.GeneratedProtocolMessageType('ZRegisterResp', (_message.Message,), dict(
  DESCRIPTOR = _ZREGISTERRESP,
  __module__ = 'register_pb2'
  # @@protoc_insertion_point(class_scope:ZRegisterResp)
  ))
_sym_db.RegisterMessage(ZRegisterResp)

ZRegisterMsg = _reflection.GeneratedProtocolMessageType('ZRegisterMsg', (_message.Message,), dict(
  DESCRIPTOR = _ZREGISTERMSG,
  __module__ = 'register_pb2'
  # @@protoc_insertion_point(class_scope:ZRegisterMsg)
  ))
_sym_db.RegisterMessage(ZRegisterMsg)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)