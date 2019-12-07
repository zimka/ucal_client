# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cserver.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x17\n\x07JsonMsg\x12\x0c\n\x04json\x18\x01 \x01(\t\"s\n\x08\x42lockMsg\x12\x15\n\rwrite_step_tu\x18\x01 \x01(\x07\x12\x14\n\x0c\x62lock_len_tu\x18\x02 \x01(\x07\x12\x14\n\x0cread_step_tu\x18\x03 \x01(\x01\x12\x11\n\tvoltage_0\x18\x04 \x03(\x11\x12\x11\n\tvoltage_1\x18\x05 \x03(\x11\"+\n\x0cTimeStampMsg\x12\x0c\n\x04step\x18\x01 \x01(\x07\x12\r\n\x05\x63ount\x18\x02 \x01(\x07\"\xb5\x01\n\x08\x46rameMsg\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.FrameMsg.DataEntry\x12\x19\n\x02ts\x18\x02 \x01(\x0b\x32\r.TimeStampMsg\x12\x0c\n\x04size\x18\x03 \x01(\x07\x1a\x1a\n\nSignalData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\x1a\x41\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.FrameMsg.SignalData:\x02\x38\x01\"&\n\x08StateMsg\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x07\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x07\n\x05OkMsg\"\x15\n\x06LogMsg\x12\x0b\n\x03row\x18\x01 \x03(\t2\xbb\x03\n\x06Server\x12/\n\tGetConfig\x12\x16.google.protobuf.Empty\x1a\x08.JsonMsg\"\x00\x12\x30\n\x07GetPlan\x12\x16.google.protobuf.Empty\x1a\t.BlockMsg\"\x00\x30\x01\x12\'\n\x07GetData\x12\r.TimeStampMsg\x1a\t.FrameMsg\"\x00\x30\x01\x12/\n\x08GetState\x12\x16.google.protobuf.Empty\x1a\t.StateMsg\"\x00\x12 \n\x07SetPlan\x12\t.BlockMsg\x1a\x06.OkMsg\"\x00(\x01\x12\x1f\n\tSetConfig\x12\x08.JsonMsg\x1a\x06.OkMsg\"\x00\x12+\n\x07RunNext\x12\x16.google.protobuf.Empty\x1a\x06.OkMsg\"\x00\x12(\n\x04Stop\x12\x16.google.protobuf.Empty\x1a\x06.OkMsg\"\x00\x12,\n\x07GetLogs\x12\x16.google.protobuf.Empty\x1a\x07.LogMsg\"\x00\x12,\n\x08\x44ropLogs\x12\x16.google.protobuf.Empty\x1a\x06.OkMsg\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_JSONMSG = _descriptor.Descriptor(
  name='JsonMsg',
  full_name='JsonMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='JsonMsg.json', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=68,
)


_BLOCKMSG = _descriptor.Descriptor(
  name='BlockMsg',
  full_name='BlockMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='write_step_tu', full_name='BlockMsg.write_step_tu', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_len_tu', full_name='BlockMsg.block_len_tu', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_step_tu', full_name='BlockMsg.read_step_tu', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltage_0', full_name='BlockMsg.voltage_0', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltage_1', full_name='BlockMsg.voltage_1', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=70,
  serialized_end=185,
)


_TIMESTAMPMSG = _descriptor.Descriptor(
  name='TimeStampMsg',
  full_name='TimeStampMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='TimeStampMsg.step', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='TimeStampMsg.count', index=1,
      number=2, type=7, cpp_type=3, label=1,
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
  serialized_start=187,
  serialized_end=230,
)


_FRAMEMSG_SIGNALDATA = _descriptor.Descriptor(
  name='SignalData',
  full_name='FrameMsg.SignalData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='FrameMsg.SignalData.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=321,
  serialized_end=347,
)

_FRAMEMSG_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='FrameMsg.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='FrameMsg.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='FrameMsg.DataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=414,
)

_FRAMEMSG = _descriptor.Descriptor(
  name='FrameMsg',
  full_name='FrameMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='FrameMsg.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='FrameMsg.ts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='FrameMsg.size', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FRAMEMSG_SIGNALDATA, _FRAMEMSG_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=414,
)


_STATEMSG = _descriptor.Descriptor(
  name='StateMsg',
  full_name='StateMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='StateMsg.code', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='StateMsg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=416,
  serialized_end=454,
)


_OKMSG = _descriptor.Descriptor(
  name='OkMsg',
  full_name='OkMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=456,
  serialized_end=463,
)


_LOGMSG = _descriptor.Descriptor(
  name='LogMsg',
  full_name='LogMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='LogMsg.row', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=465,
  serialized_end=486,
)

_FRAMEMSG_SIGNALDATA.containing_type = _FRAMEMSG
_FRAMEMSG_DATAENTRY.fields_by_name['value'].message_type = _FRAMEMSG_SIGNALDATA
_FRAMEMSG_DATAENTRY.containing_type = _FRAMEMSG
_FRAMEMSG.fields_by_name['data'].message_type = _FRAMEMSG_DATAENTRY
_FRAMEMSG.fields_by_name['ts'].message_type = _TIMESTAMPMSG
DESCRIPTOR.message_types_by_name['JsonMsg'] = _JSONMSG
DESCRIPTOR.message_types_by_name['BlockMsg'] = _BLOCKMSG
DESCRIPTOR.message_types_by_name['TimeStampMsg'] = _TIMESTAMPMSG
DESCRIPTOR.message_types_by_name['FrameMsg'] = _FRAMEMSG
DESCRIPTOR.message_types_by_name['StateMsg'] = _STATEMSG
DESCRIPTOR.message_types_by_name['OkMsg'] = _OKMSG
DESCRIPTOR.message_types_by_name['LogMsg'] = _LOGMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JsonMsg = _reflection.GeneratedProtocolMessageType('JsonMsg', (_message.Message,), {
  'DESCRIPTOR' : _JSONMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:JsonMsg)
  })
_sym_db.RegisterMessage(JsonMsg)

BlockMsg = _reflection.GeneratedProtocolMessageType('BlockMsg', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:BlockMsg)
  })
_sym_db.RegisterMessage(BlockMsg)

TimeStampMsg = _reflection.GeneratedProtocolMessageType('TimeStampMsg', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMPMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:TimeStampMsg)
  })
_sym_db.RegisterMessage(TimeStampMsg)

FrameMsg = _reflection.GeneratedProtocolMessageType('FrameMsg', (_message.Message,), {

  'SignalData' : _reflection.GeneratedProtocolMessageType('SignalData', (_message.Message,), {
    'DESCRIPTOR' : _FRAMEMSG_SIGNALDATA,
    '__module__' : 'server_pb2'
    # @@protoc_insertion_point(class_scope:FrameMsg.SignalData)
    })
  ,

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _FRAMEMSG_DATAENTRY,
    '__module__' : 'server_pb2'
    # @@protoc_insertion_point(class_scope:FrameMsg.DataEntry)
    })
  ,
  'DESCRIPTOR' : _FRAMEMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:FrameMsg)
  })
_sym_db.RegisterMessage(FrameMsg)
_sym_db.RegisterMessage(FrameMsg.SignalData)
_sym_db.RegisterMessage(FrameMsg.DataEntry)

StateMsg = _reflection.GeneratedProtocolMessageType('StateMsg', (_message.Message,), {
  'DESCRIPTOR' : _STATEMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:StateMsg)
  })
_sym_db.RegisterMessage(StateMsg)

OkMsg = _reflection.GeneratedProtocolMessageType('OkMsg', (_message.Message,), {
  'DESCRIPTOR' : _OKMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:OkMsg)
  })
_sym_db.RegisterMessage(OkMsg)

LogMsg = _reflection.GeneratedProtocolMessageType('LogMsg', (_message.Message,), {
  'DESCRIPTOR' : _LOGMSG,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:LogMsg)
  })
_sym_db.RegisterMessage(LogMsg)


_FRAMEMSG_DATAENTRY._options = None

_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='Server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=489,
  serialized_end=932,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='Server.GetConfig',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_JSONMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlan',
    full_name='Server.GetPlan',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BLOCKMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='Server.GetData',
    index=2,
    containing_service=None,
    input_type=_TIMESTAMPMSG,
    output_type=_FRAMEMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='Server.GetState',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_STATEMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetPlan',
    full_name='Server.SetPlan',
    index=4,
    containing_service=None,
    input_type=_BLOCKMSG,
    output_type=_OKMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfig',
    full_name='Server.SetConfig',
    index=5,
    containing_service=None,
    input_type=_JSONMSG,
    output_type=_OKMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RunNext',
    full_name='Server.RunNext',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_OKMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='Server.Stop',
    index=7,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_OKMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLogs',
    full_name='Server.GetLogs',
    index=8,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LOGMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropLogs',
    full_name='Server.DropLogs',
    index=9,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_OKMSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)