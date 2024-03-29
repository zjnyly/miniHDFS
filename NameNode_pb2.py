# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NameNode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NameNode.proto',
  package='NameNode',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eNameNode.proto\x12\x08NameNode\"\x12\n\x03msg\x12\x0b\n\x03msg\x18\x01 \x01(\t\"6\n\x05\x63pMsg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0f\n\x07\x63urrent\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x01(\t\".\n\x08userInfo\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"[\n\x08\x66ileInfo\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x10\n\x08\x66ileSize\x18\x03 \x01(\x03\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\t\x12\r\n\x05share\x18\x05 \x01(\x08\"L\n\x0cinstructions\x12\r\n\x05\x61llow\x18\x01 \x01(\x08\x12\x0e\n\x06giveTo\x18\x02 \x01(\t\x12\x0e\n\x06\x63hunks\x18\x03 \x01(\x05\x12\r\n\x05howTo\x18\x04 \x01(\t\"/\n\x0c\x64\x61taNodeInfo\x12\x10\n\x08nodeName\x18\x01 \x01(\t\x12\r\n\x05space\x18\x02 \x01(\x05\x32\xc9\x05\n\x08NameNode\x12\x35\n\x13\x63heckNameNodeStatus\x12\r.NameNode.msg\x1a\r.NameNode.msg\"\x00\x12\x31\n\nbindClient\x12\x12.NameNode.userInfo\x1a\r.NameNode.msg\"\x00\x12/\n\x08register\x12\x12.NameNode.userInfo\x1a\r.NameNode.msg\"\x00\x12%\n\x03pwd\x12\r.NameNode.msg\x1a\r.NameNode.msg\"\x00\x12\'\n\x05mkdir\x12\r.NameNode.msg\x1a\r.NameNode.msg\"\x00\x12$\n\x02\x63\x64\x12\r.NameNode.msg\x1a\r.NameNode.msg\"\x00\x12\x36\n\x06upload\x12\x12.NameNode.fileInfo\x1a\x16.NameNode.instructions\"\x00\x12-\n\x06\x64\x65lete\x12\x12.NameNode.fileInfo\x1a\r.NameNode.msg\"\x00\x12\'\n\x05\x65rror\x12\r.NameNode.msg\x1a\r.NameNode.msg\"\x00\x12\x38\n\x08\x64ownload\x12\x12.NameNode.fileInfo\x1a\x16.NameNode.instructions\"\x00\x12/\n\x08readfile\x12\x12.NameNode.fileInfo\x1a\r.NameNode.msg\"\x00\x12\x32\n\x0breleasefile\x12\x12.NameNode.fileInfo\x1a\r.NameNode.msg\"\x00\x12$\n\x02ls\x12\r.NameNode.msg\x1a\r.NameNode.msg\"\x00\x12&\n\x02\x63p\x12\x0f.NameNode.cpMsg\x1a\r.NameNode.msg\"\x00\x12/\n\x04join\x12\x16.NameNode.dataNodeInfo\x1a\r.NameNode.msg\"\x00\x62\x06proto3'
)




_MSG = _descriptor.Descriptor(
  name='msg',
  full_name='NameNode.msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='NameNode.msg.msg', index=0,
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


_CPMSG = _descriptor.Descriptor(
  name='cpMsg',
  full_name='NameNode.cpMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='NameNode.cpMsg.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current', full_name='NameNode.cpMsg.current', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='NameNode.cpMsg.to', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=102,
)


_USERINFO = _descriptor.Descriptor(
  name='userInfo',
  full_name='NameNode.userInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='NameNode.userInfo.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='NameNode.userInfo.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=104,
  serialized_end=150,
)


_FILEINFO = _descriptor.Descriptor(
  name='fileInfo',
  full_name='NameNode.fileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='NameNode.fileInfo.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='NameNode.fileInfo.to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileSize', full_name='NameNode.fileInfo.fileSize', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='NameNode.fileInfo.checksum', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='share', full_name='NameNode.fileInfo.share', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=152,
  serialized_end=243,
)


_INSTRUCTIONS = _descriptor.Descriptor(
  name='instructions',
  full_name='NameNode.instructions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow', full_name='NameNode.instructions.allow', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='giveTo', full_name='NameNode.instructions.giveTo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='NameNode.instructions.chunks', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='howTo', full_name='NameNode.instructions.howTo', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=245,
  serialized_end=321,
)


_DATANODEINFO = _descriptor.Descriptor(
  name='dataNodeInfo',
  full_name='NameNode.dataNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeName', full_name='NameNode.dataNodeInfo.nodeName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='space', full_name='NameNode.dataNodeInfo.space', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=323,
  serialized_end=370,
)

DESCRIPTOR.message_types_by_name['msg'] = _MSG
DESCRIPTOR.message_types_by_name['cpMsg'] = _CPMSG
DESCRIPTOR.message_types_by_name['userInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['fileInfo'] = _FILEINFO
DESCRIPTOR.message_types_by_name['instructions'] = _INSTRUCTIONS
DESCRIPTOR.message_types_by_name['dataNodeInfo'] = _DATANODEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

msg = _reflection.GeneratedProtocolMessageType('msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'NameNode_pb2'
  # @@protoc_insertion_point(class_scope:NameNode.msg)
  })
_sym_db.RegisterMessage(msg)

cpMsg = _reflection.GeneratedProtocolMessageType('cpMsg', (_message.Message,), {
  'DESCRIPTOR' : _CPMSG,
  '__module__' : 'NameNode_pb2'
  # @@protoc_insertion_point(class_scope:NameNode.cpMsg)
  })
_sym_db.RegisterMessage(cpMsg)

userInfo = _reflection.GeneratedProtocolMessageType('userInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'NameNode_pb2'
  # @@protoc_insertion_point(class_scope:NameNode.userInfo)
  })
_sym_db.RegisterMessage(userInfo)

fileInfo = _reflection.GeneratedProtocolMessageType('fileInfo', (_message.Message,), {
  'DESCRIPTOR' : _FILEINFO,
  '__module__' : 'NameNode_pb2'
  # @@protoc_insertion_point(class_scope:NameNode.fileInfo)
  })
_sym_db.RegisterMessage(fileInfo)

instructions = _reflection.GeneratedProtocolMessageType('instructions', (_message.Message,), {
  'DESCRIPTOR' : _INSTRUCTIONS,
  '__module__' : 'NameNode_pb2'
  # @@protoc_insertion_point(class_scope:NameNode.instructions)
  })
_sym_db.RegisterMessage(instructions)

dataNodeInfo = _reflection.GeneratedProtocolMessageType('dataNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATANODEINFO,
  '__module__' : 'NameNode_pb2'
  # @@protoc_insertion_point(class_scope:NameNode.dataNodeInfo)
  })
_sym_db.RegisterMessage(dataNodeInfo)



_NAMENODE = _descriptor.ServiceDescriptor(
  name='NameNode',
  full_name='NameNode.NameNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=373,
  serialized_end=1086,
  methods=[
  _descriptor.MethodDescriptor(
    name='checkNameNodeStatus',
    full_name='NameNode.NameNode.checkNameNodeStatus',
    index=0,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='bindClient',
    full_name='NameNode.NameNode.bindClient',
    index=1,
    containing_service=None,
    input_type=_USERINFO,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='register',
    full_name='NameNode.NameNode.register',
    index=2,
    containing_service=None,
    input_type=_USERINFO,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pwd',
    full_name='NameNode.NameNode.pwd',
    index=3,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='mkdir',
    full_name='NameNode.NameNode.mkdir',
    index=4,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='cd',
    full_name='NameNode.NameNode.cd',
    index=5,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='upload',
    full_name='NameNode.NameNode.upload',
    index=6,
    containing_service=None,
    input_type=_FILEINFO,
    output_type=_INSTRUCTIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='NameNode.NameNode.delete',
    index=7,
    containing_service=None,
    input_type=_FILEINFO,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='error',
    full_name='NameNode.NameNode.error',
    index=8,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='download',
    full_name='NameNode.NameNode.download',
    index=9,
    containing_service=None,
    input_type=_FILEINFO,
    output_type=_INSTRUCTIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='readfile',
    full_name='NameNode.NameNode.readfile',
    index=10,
    containing_service=None,
    input_type=_FILEINFO,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='releasefile',
    full_name='NameNode.NameNode.releasefile',
    index=11,
    containing_service=None,
    input_type=_FILEINFO,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ls',
    full_name='NameNode.NameNode.ls',
    index=12,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='cp',
    full_name='NameNode.NameNode.cp',
    index=13,
    containing_service=None,
    input_type=_CPMSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='join',
    full_name='NameNode.NameNode.join',
    index=14,
    containing_service=None,
    input_type=_DATANODEINFO,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NAMENODE)

DESCRIPTOR.services_by_name['NameNode'] = _NAMENODE

# @@protoc_insertion_point(module_scope)
