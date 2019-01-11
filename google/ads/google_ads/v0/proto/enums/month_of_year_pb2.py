# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/month_of_year.proto

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
  name='google/ads/googleads_v0/proto/enums/month_of_year.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n7google/ads/googleads_v0/proto/enums/month_of_year.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xd1\x01\n\x0fMonthOfYearEnum\"\xbd\x01\n\x0bMonthOfYear\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07JANUARY\x10\x02\x12\x0c\n\x08\x46\x45\x42RUARY\x10\x03\x12\t\n\x05MARCH\x10\x04\x12\t\n\x05\x41PRIL\x10\x05\x12\x07\n\x03MAY\x10\x06\x12\x08\n\x04JUNE\x10\x07\x12\x08\n\x04JULY\x10\x08\x12\n\n\x06\x41UGUST\x10\t\x12\r\n\tSEPTEMBER\x10\n\x12\x0b\n\x07OCTOBER\x10\x0b\x12\x0c\n\x08NOVEMBER\x10\x0c\x12\x0c\n\x08\x44\x45\x43\x45MBER\x10\rB\xc1\x01\n!com.google.ads.googleads.v0.enumsB\x10MonthOfYearProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_MONTHOFYEARENUM_MONTHOFYEAR = _descriptor.EnumDescriptor(
  name='MonthOfYear',
  full_name='google.ads.googleads.v0.enums.MonthOfYearEnum.MonthOfYear',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JANUARY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEBRUARY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARCH', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APRIL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAY', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JUNE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JULY', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUGUST', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEPTEMBER', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OCTOBER', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVEMBER', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECEMBER', index=13, number=13,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=111,
  serialized_end=300,
)
_sym_db.RegisterEnumDescriptor(_MONTHOFYEARENUM_MONTHOFYEAR)


_MONTHOFYEARENUM = _descriptor.Descriptor(
  name='MonthOfYearEnum',
  full_name='google.ads.googleads.v0.enums.MonthOfYearEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MONTHOFYEARENUM_MONTHOFYEAR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=300,
)

_MONTHOFYEARENUM_MONTHOFYEAR.containing_type = _MONTHOFYEARENUM
DESCRIPTOR.message_types_by_name['MonthOfYearEnum'] = _MONTHOFYEARENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MonthOfYearEnum = _reflection.GeneratedProtocolMessageType('MonthOfYearEnum', (_message.Message,), dict(
  DESCRIPTOR = _MONTHOFYEARENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.month_of_year_pb2'
  ,
  __doc__ = """Container for enumeration of months of the year, e.g., "January".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.MonthOfYearEnum)
  ))
_sym_db.RegisterMessage(MonthOfYearEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\020MonthOfYearProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)