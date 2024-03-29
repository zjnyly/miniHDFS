# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataNode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DataNode.proto',
  package='DataNode',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x44\x61taNode.proto\x12\x08\x44\x61taNode\"\x12\n\x03msg\x12\x0b\n\x03msg\x18\x01 \x01(\t\"2\n\nuploadFile\x12\x14\n\x0cinstructions\x18\x01 \x01(\t\x12\x0e\n\x06\x62uffer\x18\x02 \x01(\x0c\"*\n\x08saveFile\x12\x0e\n\x06\x66ileID\x18\x01 \x01(\t\x12\x0e\n\x06\x62uffer\x18\x02 \x01(\x0c\x32\xf6\x01\n\x08\x44\x61taNode\x12+\n\theartbeat\x12\r.DataNode.msg\x1a\r.DataNode.msg\"\x00\x12\x31\n\x06upload\x12\x14.DataNode.uploadFile\x1a\r.DataNode.msg\"\x00(\x01\x12\x32\n\x07replica\x12\x14.DataNode.uploadFile\x1a\r.DataNode.msg\"\x00(\x01\x12,\n\x03get\x12\r.DataNode.msg\x1a\x12.DataNode.saveFile\"\x00\x30\x01\x12(\n\x06remove\x12\r.DataNode.msg\x1a\r.DataNode.msg\"\x00\x62\x06proto3'
)




_MSG = _descriptor.Descriptor(
  name='msg',
  full_name='DataNode.msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='DataNode.msg.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=46,
)


_UPLOADFILE = _descriptor.Descriptor(
  name='uploadFile',
  full_name='DataNode.uploadFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instructions', full_name='DataNode.uploadFile.instructions', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffer', full_name='DataNode.uploadFile.buffer', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=48,
  serialized_end=98,
)


_SAVEFILE = _descriptor.Descriptor(
  name='saveFile',
  full_name='DataNode.saveFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileID', full_name='DataNode.saveFile.fileID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffer', full_name='DataNode.saveFile.buffer', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=100,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['msg'] = _MSG
DESCRIPTOR.message_types_by_name['uploadFile'] = _UPLOADFILE
DESCRIPTOR.message_types_by_name['saveFile'] = _SAVEFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

msg = _reflection.GeneratedProtocolMessageType('msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'DataNode_pb2'
  # @@protoc_insertion_point(class_scope:DataNode.msg)
  })
_sym_db.RegisterMessage(msg)

uploadFile = _reflection.GeneratedProtocolMessageType('uploadFile', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILE,
  '__module__' : 'DataNode_pb2'
  # @@protoc_insertion_point(class_scope:DataNode.uploadFile)
  })
_sym_db.RegisterMessage(uploadFile)

saveFile = _reflection.GeneratedProtocolMessageType('saveFile', (_message.Message,), {
  'DESCRIPTOR' : _SAVEFILE,
  '__module__' : 'DataNode_pb2'
  # @@protoc_insertion_point(class_scope:DataNode.saveFile)
  })
_sym_db.RegisterMessage(saveFile)



_DATANODE = _descriptor.ServiceDescriptor(
  name='DataNode',
  full_name='DataNode.DataNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=145,
  serialized_end=391,
  methods=[
  _descriptor.MethodDescriptor(
    name='heartbeat',
    full_name='DataNode.DataNode.heartbeat',
    index=0,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='upload',
    full_name='DataNode.DataNode.upload',
    index=1,
    containing_service=None,
    input_type=_UPLOADFILE,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='replica',
    full_name='DataNode.DataNode.replica',
    index=2,
    containing_service=None,
    input_type=_UPLOADFILE,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='DataNode.DataNode.get',
    index=3,
    containing_service=None,
    input_type=_MSG,
    output_type=_SAVEFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='remove',
    full_name='DataNode.DataNode.remove',
    index=4,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATANODE)

DESCRIPTOR.services_by_name['DataNode'] = _DATANODE

# @@protoc_insertion_point(module_scope)
