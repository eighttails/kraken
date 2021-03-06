# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clstm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='clstm.proto',
  package='clstm',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x63lstm.proto\x12\x05\x63lstm\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"1\n\x05\x41rray\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64im\x18\x02 \x03(\x05\x12\r\n\x05value\x18\x03 \x03(\x02\"\xcf\x01\n\x0cNetworkProto\x12\x0c\n\x04kind\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06ninput\x18\n \x02(\x05\x12\x0f\n\x07noutput\x18\x0b \x02(\x05\x12\x0e\n\x06icodec\x18\x0c \x03(\x05\x12\r\n\x05\x63odec\x18\r \x03(\x05\x12\"\n\tattribute\x18\x14 \x03(\x0b\x32\x0f.clstm.KeyValue\x12\x1d\n\x07weights\x18\x1e \x03(\x0b\x32\x0c.clstm.Array\x12 \n\x03sub\x18( \x03(\x0b\x32\x13.clstm.NetworkProto')
)




_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='clstm.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='clstm.KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='clstm.KeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=60,
)


_ARRAY = _descriptor.Descriptor(
  name='Array',
  full_name='clstm.Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='clstm.Array.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dim', full_name='clstm.Array.dim', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='clstm.Array.value', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=111,
)


_NETWORKPROTO = _descriptor.Descriptor(
  name='NetworkProto',
  full_name='clstm.NetworkProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='clstm.NetworkProto.kind', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='clstm.NetworkProto.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ninput', full_name='clstm.NetworkProto.ninput', index=2,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noutput', full_name='clstm.NetworkProto.noutput', index=3,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icodec', full_name='clstm.NetworkProto.icodec', index=4,
      number=12, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='codec', full_name='clstm.NetworkProto.codec', index=5,
      number=13, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='clstm.NetworkProto.attribute', index=6,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weights', full_name='clstm.NetworkProto.weights', index=7,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub', full_name='clstm.NetworkProto.sub', index=8,
      number=40, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=321,
)

_NETWORKPROTO.fields_by_name['attribute'].message_type = _KEYVALUE
_NETWORKPROTO.fields_by_name['weights'].message_type = _ARRAY
_NETWORKPROTO.fields_by_name['sub'].message_type = _NETWORKPROTO
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['Array'] = _ARRAY
DESCRIPTOR.message_types_by_name['NetworkProto'] = _NETWORKPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUE,
  __module__ = 'clstm_pb2'
  # @@protoc_insertion_point(class_scope:clstm.KeyValue)
  ))
_sym_db.RegisterMessage(KeyValue)

Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), dict(
  DESCRIPTOR = _ARRAY,
  __module__ = 'clstm_pb2'
  # @@protoc_insertion_point(class_scope:clstm.Array)
  ))
_sym_db.RegisterMessage(Array)

NetworkProto = _reflection.GeneratedProtocolMessageType('NetworkProto', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKPROTO,
  __module__ = 'clstm_pb2'
  # @@protoc_insertion_point(class_scope:clstm.NetworkProto)
  ))
_sym_db.RegisterMessage(NetworkProto)


# @@protoc_insertion_point(module_scope)
