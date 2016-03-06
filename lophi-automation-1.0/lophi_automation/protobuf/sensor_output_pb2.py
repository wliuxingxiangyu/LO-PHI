# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='sensor_output.proto',
  package='semantic_output',
  serialized_pb='\n\x13sensor_output.proto\x12\x0fsemantic_output\"P\n\x0cSemanticInfo\x12\x0e\n\x06MODULE\x18\x01 \x02(\t\x12\x0e\n\x06SENSOR\x18\x02 \x02(\t\x12\x0f\n\x07PROFILE\x18\x03 \x02(\t\x12\x0f\n\x07MACHINE\x18\x04 \x02(\t\"`\n\x0eSemanticHeader\x12\x36\n\x06\x63olumn\x18\x01 \x03(\x0b\x32&.semantic_output.SemanticHeader.Column\x1a\x16\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x02(\t\"W\n\x0cSemanticData\x12\x30\n\x04item\x18\x01 \x03(\x0b\x32\".semantic_output.SemanticData.Item\x1a\x15\n\x04Item\x12\r\n\x05value\x18\x01 \x02(\t\"\x9b\x01\n\x0eSemanticOutput\x12+\n\x04INFO\x18\x01 \x02(\x0b\x32\x1d.semantic_output.SemanticInfo\x12/\n\x06HEADER\x18\x02 \x02(\x0b\x32\x1f.semantic_output.SemanticHeader\x12+\n\x04\x44\x41TA\x18\x03 \x03(\x0b\x32\x1d.semantic_output.SemanticData')




_SEMANTICINFO = descriptor.Descriptor(
  name='SemanticInfo',
  full_name='semantic_output.SemanticInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='MODULE', full_name='semantic_output.SemanticInfo.MODULE', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='SENSOR', full_name='semantic_output.SemanticInfo.SENSOR', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='PROFILE', full_name='semantic_output.SemanticInfo.PROFILE', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='MACHINE', full_name='semantic_output.SemanticInfo.MACHINE', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=40,
  serialized_end=120,
)


_SEMANTICHEADER_COLUMN = descriptor.Descriptor(
  name='Column',
  full_name='semantic_output.SemanticHeader.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='semantic_output.SemanticHeader.Column.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=196,
  serialized_end=218,
)

_SEMANTICHEADER = descriptor.Descriptor(
  name='SemanticHeader',
  full_name='semantic_output.SemanticHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='column', full_name='semantic_output.SemanticHeader.column', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SEMANTICHEADER_COLUMN, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=122,
  serialized_end=218,
)


_SEMANTICDATA_ITEM = descriptor.Descriptor(
  name='Item',
  full_name='semantic_output.SemanticData.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value', full_name='semantic_output.SemanticData.Item.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=286,
  serialized_end=307,
)

_SEMANTICDATA = descriptor.Descriptor(
  name='SemanticData',
  full_name='semantic_output.SemanticData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item', full_name='semantic_output.SemanticData.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SEMANTICDATA_ITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=220,
  serialized_end=307,
)


_SEMANTICOUTPUT = descriptor.Descriptor(
  name='SemanticOutput',
  full_name='semantic_output.SemanticOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='INFO', full_name='semantic_output.SemanticOutput.INFO', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='HEADER', full_name='semantic_output.SemanticOutput.HEADER', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DATA', full_name='semantic_output.SemanticOutput.DATA', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=310,
  serialized_end=465,
)

_SEMANTICHEADER_COLUMN.containing_type = _SEMANTICHEADER;
_SEMANTICHEADER.fields_by_name['column'].message_type = _SEMANTICHEADER_COLUMN
_SEMANTICDATA_ITEM.containing_type = _SEMANTICDATA;
_SEMANTICDATA.fields_by_name['item'].message_type = _SEMANTICDATA_ITEM
_SEMANTICOUTPUT.fields_by_name['INFO'].message_type = _SEMANTICINFO
_SEMANTICOUTPUT.fields_by_name['HEADER'].message_type = _SEMANTICHEADER
_SEMANTICOUTPUT.fields_by_name['DATA'].message_type = _SEMANTICDATA
DESCRIPTOR.message_types_by_name['SemanticInfo'] = _SEMANTICINFO
DESCRIPTOR.message_types_by_name['SemanticHeader'] = _SEMANTICHEADER
DESCRIPTOR.message_types_by_name['SemanticData'] = _SEMANTICDATA
DESCRIPTOR.message_types_by_name['SemanticOutput'] = _SEMANTICOUTPUT

class SemanticInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SEMANTICINFO
  
  # @@protoc_insertion_point(class_scope:semantic_output.SemanticInfo)

class SemanticHeader(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Column(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEMANTICHEADER_COLUMN
    
    # @@protoc_insertion_point(class_scope:semantic_output.SemanticHeader.Column)
  DESCRIPTOR = _SEMANTICHEADER
  
  # @@protoc_insertion_point(class_scope:semantic_output.SemanticHeader)

class SemanticData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Item(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEMANTICDATA_ITEM
    
    # @@protoc_insertion_point(class_scope:semantic_output.SemanticData.Item)
  DESCRIPTOR = _SEMANTICDATA
  
  # @@protoc_insertion_point(class_scope:semantic_output.SemanticData)

class SemanticOutput(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SEMANTICOUTPUT
  
  # @@protoc_insertion_point(class_scope:semantic_output.SemanticOutput)

# @@protoc_insertion_point(module_scope)
