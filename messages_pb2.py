# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0emessages.proto\"6\n\x0cSpeedCommand\x12\n\n\x02vx\x18\x01 \x02(\x02\x12\n\n\x02vy\x18\x02 \x01(\x02\x12\x0e\n\x06vtheta\x18\x03 \x02(\x02\"1\n\nPosCommand\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\r\n\x05theta\x18\x03 \x01(\x02\"=\n\nOdomReport\x12\r\n\x05pos_x\x18\x01 \x02(\x02\x12\r\n\x05pos_y\x18\x02 \x02(\x02\x12\x11\n\tpos_theta\x18\x03 \x02(\x02\"%\n\x03IHM\x12\x0f\n\x07tirette\x18\x01 \x02(\x08\x12\r\n\x05\x63olor\x18\x02 \x02(\x08\"+\n\x0b\x42uoyCatcher\x12\x0e\n\x06height\x18\x01 \x02(\x05\x12\x0c\n\x04grab\x18\x02 \x02(\x08\"\x18\n\tFlagServo\x12\x0b\n\x03pos\x18\x01 \x02(\x05')
)




_SPEEDCOMMAND = _descriptor.Descriptor(
  name='SpeedCommand',
  full_name='SpeedCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vx', full_name='SpeedCommand.vx', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vy', full_name='SpeedCommand.vy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vtheta', full_name='SpeedCommand.vtheta', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=72,
)


_POSCOMMAND = _descriptor.Descriptor(
  name='PosCommand',
  full_name='PosCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PosCommand.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='PosCommand.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theta', full_name='PosCommand.theta', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=123,
)


_ODOMREPORT = _descriptor.Descriptor(
  name='OdomReport',
  full_name='OdomReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='OdomReport.pos_x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='OdomReport.pos_y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_theta', full_name='OdomReport.pos_theta', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=186,
)


_IHM = _descriptor.Descriptor(
  name='IHM',
  full_name='IHM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tirette', full_name='IHM.tirette', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='IHM.color', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=225,
)


_BUOYCATCHER = _descriptor.Descriptor(
  name='BuoyCatcher',
  full_name='BuoyCatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='BuoyCatcher.height', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grab', full_name='BuoyCatcher.grab', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=270,
)


_FLAGSERVO = _descriptor.Descriptor(
  name='FlagServo',
  full_name='FlagServo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='FlagServo.pos', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=296,
)

DESCRIPTOR.message_types_by_name['SpeedCommand'] = _SPEEDCOMMAND
DESCRIPTOR.message_types_by_name['PosCommand'] = _POSCOMMAND
DESCRIPTOR.message_types_by_name['OdomReport'] = _ODOMREPORT
DESCRIPTOR.message_types_by_name['IHM'] = _IHM
DESCRIPTOR.message_types_by_name['BuoyCatcher'] = _BUOYCATCHER
DESCRIPTOR.message_types_by_name['FlagServo'] = _FLAGSERVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpeedCommand = _reflection.GeneratedProtocolMessageType('SpeedCommand', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDCOMMAND,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:SpeedCommand)
  ))
_sym_db.RegisterMessage(SpeedCommand)

PosCommand = _reflection.GeneratedProtocolMessageType('PosCommand', (_message.Message,), dict(
  DESCRIPTOR = _POSCOMMAND,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:PosCommand)
  ))
_sym_db.RegisterMessage(PosCommand)

OdomReport = _reflection.GeneratedProtocolMessageType('OdomReport', (_message.Message,), dict(
  DESCRIPTOR = _ODOMREPORT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:OdomReport)
  ))
_sym_db.RegisterMessage(OdomReport)

IHM = _reflection.GeneratedProtocolMessageType('IHM', (_message.Message,), dict(
  DESCRIPTOR = _IHM,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:IHM)
  ))
_sym_db.RegisterMessage(IHM)

BuoyCatcher = _reflection.GeneratedProtocolMessageType('BuoyCatcher', (_message.Message,), dict(
  DESCRIPTOR = _BUOYCATCHER,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:BuoyCatcher)
  ))
_sym_db.RegisterMessage(BuoyCatcher)

FlagServo = _reflection.GeneratedProtocolMessageType('FlagServo', (_message.Message,), dict(
  DESCRIPTOR = _FLAGSERVO,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:FlagServo)
  ))
_sym_db.RegisterMessage(FlagServo)


# @@protoc_insertion_point(module_scope)
