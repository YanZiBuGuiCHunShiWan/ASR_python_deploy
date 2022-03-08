# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stt.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tstt.proto\"X\n\x10RecognizeRequest\x12\"\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x12.RecognitionConfig\x12 \n\x05\x61udio\x18\x02 \x01(\x0b\x32\x11.RecognitionAudio\"o\n\x19StreamingRecognizeRequest\x12$\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x12.RecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"@\n\x1aStreamingRecognitionConfig\x12\"\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x12.RecognitionConfig\"/\n\x11RecognitionConfig\x12\x1a\n\x11sample_rate_hertz\x18\x80} \x01(\x05\"5\n\x10RecognitionAudio\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x42\x0e\n\x0c\x61udio_source\"\'\n\x11RecognizeResponse\x12\x12\n\ntranscript\x18\x01 \x01(\t\"0\n\x1aStreamingRecognizeResponse\x12\x12\n\ntranscript\x18\x01 \x01(\t\"0\n\x1aStreamingRecognitionResult\x12\x12\n\ntranscript\x18\x01 \x01(\t\"-\n\x17SpeechRecognitionResult\x12\x12\n\ntranscript\x18\x01 \x01(\t2\x90\x01\n\x03STT\x12\x34\n\tRecognize\x12\x11.RecognizeRequest\x1a\x12.RecognizeResponse\"\x00\x12S\n\x12StreamingRecognize\x12\x1a.StreamingRecognizeRequest\x1a\x1b.StreamingRecognizeResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_RECOGNIZEREQUEST = _descriptor.Descriptor(
  name='RecognizeRequest',
  full_name='RecognizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='RecognizeRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio', full_name='RecognizeRequest.audio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=13,
  serialized_end=101,
)


_STREAMINGRECOGNIZEREQUEST = _descriptor.Descriptor(
  name='StreamingRecognizeRequest',
  full_name='StreamingRecognizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='StreamingRecognizeRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_content', full_name='StreamingRecognizeRequest.audio_content', index=1,
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
    _descriptor.OneofDescriptor(
      name='streaming_request', full_name='StreamingRecognizeRequest.streaming_request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=103,
  serialized_end=214,
)


_STREAMINGRECOGNITIONCONFIG = _descriptor.Descriptor(
  name='StreamingRecognitionConfig',
  full_name='StreamingRecognitionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='StreamingRecognitionConfig.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=216,
  serialized_end=280,
)


_RECOGNITIONCONFIG = _descriptor.Descriptor(
  name='RecognitionConfig',
  full_name='RecognitionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='RecognitionConfig.sample_rate_hertz', index=0,
      number=16000, type=5, cpp_type=1, label=1,
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
  serialized_start=282,
  serialized_end=329,
)


_RECOGNITIONAUDIO = _descriptor.Descriptor(
  name='RecognitionAudio',
  full_name='RecognitionAudio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='RecognitionAudio.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='audio_source', full_name='RecognitionAudio.audio_source',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=331,
  serialized_end=384,
)


_RECOGNIZERESPONSE = _descriptor.Descriptor(
  name='RecognizeResponse',
  full_name='RecognizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcript', full_name='RecognizeResponse.transcript', index=0,
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
  serialized_start=386,
  serialized_end=425,
)


_STREAMINGRECOGNIZERESPONSE = _descriptor.Descriptor(
  name='StreamingRecognizeResponse',
  full_name='StreamingRecognizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcript', full_name='StreamingRecognizeResponse.transcript', index=0,
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
  serialized_start=427,
  serialized_end=475,
)


_STREAMINGRECOGNITIONRESULT = _descriptor.Descriptor(
  name='StreamingRecognitionResult',
  full_name='StreamingRecognitionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcript', full_name='StreamingRecognitionResult.transcript', index=0,
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
  serialized_start=477,
  serialized_end=525,
)


_SPEECHRECOGNITIONRESULT = _descriptor.Descriptor(
  name='SpeechRecognitionResult',
  full_name='SpeechRecognitionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcript', full_name='SpeechRecognitionResult.transcript', index=0,
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
  serialized_start=527,
  serialized_end=572,
)

_RECOGNIZEREQUEST.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_RECOGNIZEREQUEST.fields_by_name['audio'].message_type = _RECOGNITIONAUDIO
_STREAMINGRECOGNIZEREQUEST.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_STREAMINGRECOGNIZEREQUEST.oneofs_by_name['streaming_request'].fields.append(
  _STREAMINGRECOGNIZEREQUEST.fields_by_name['config'])
_STREAMINGRECOGNIZEREQUEST.fields_by_name['config'].containing_oneof = _STREAMINGRECOGNIZEREQUEST.oneofs_by_name['streaming_request']
_STREAMINGRECOGNIZEREQUEST.oneofs_by_name['streaming_request'].fields.append(
  _STREAMINGRECOGNIZEREQUEST.fields_by_name['audio_content'])
_STREAMINGRECOGNIZEREQUEST.fields_by_name['audio_content'].containing_oneof = _STREAMINGRECOGNIZEREQUEST.oneofs_by_name['streaming_request']
_STREAMINGRECOGNITIONCONFIG.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_RECOGNITIONAUDIO.oneofs_by_name['audio_source'].fields.append(
  _RECOGNITIONAUDIO.fields_by_name['content'])
_RECOGNITIONAUDIO.fields_by_name['content'].containing_oneof = _RECOGNITIONAUDIO.oneofs_by_name['audio_source']
DESCRIPTOR.message_types_by_name['RecognizeRequest'] = _RECOGNIZEREQUEST
DESCRIPTOR.message_types_by_name['StreamingRecognizeRequest'] = _STREAMINGRECOGNIZEREQUEST
DESCRIPTOR.message_types_by_name['StreamingRecognitionConfig'] = _STREAMINGRECOGNITIONCONFIG
DESCRIPTOR.message_types_by_name['RecognitionConfig'] = _RECOGNITIONCONFIG
DESCRIPTOR.message_types_by_name['RecognitionAudio'] = _RECOGNITIONAUDIO
DESCRIPTOR.message_types_by_name['RecognizeResponse'] = _RECOGNIZERESPONSE
DESCRIPTOR.message_types_by_name['StreamingRecognizeResponse'] = _STREAMINGRECOGNIZERESPONSE
DESCRIPTOR.message_types_by_name['StreamingRecognitionResult'] = _STREAMINGRECOGNITIONRESULT
DESCRIPTOR.message_types_by_name['SpeechRecognitionResult'] = _SPEECHRECOGNITIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecognizeRequest = _reflection.GeneratedProtocolMessageType('RecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZEREQUEST,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:RecognizeRequest)
  })
_sym_db.RegisterMessage(RecognizeRequest)

StreamingRecognizeRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZEREQUEST,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:StreamingRecognizeRequest)
  })
_sym_db.RegisterMessage(StreamingRecognizeRequest)

StreamingRecognitionConfig = _reflection.GeneratedProtocolMessageType('StreamingRecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONCONFIG,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:StreamingRecognitionConfig)
  })
_sym_db.RegisterMessage(StreamingRecognitionConfig)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONCONFIG,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:RecognitionConfig)
  })
_sym_db.RegisterMessage(RecognitionConfig)

RecognitionAudio = _reflection.GeneratedProtocolMessageType('RecognitionAudio', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONAUDIO,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:RecognitionAudio)
  })
_sym_db.RegisterMessage(RecognitionAudio)

RecognizeResponse = _reflection.GeneratedProtocolMessageType('RecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZERESPONSE,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:RecognizeResponse)
  })
_sym_db.RegisterMessage(RecognizeResponse)

StreamingRecognizeResponse = _reflection.GeneratedProtocolMessageType('StreamingRecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZERESPONSE,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:StreamingRecognizeResponse)
  })
_sym_db.RegisterMessage(StreamingRecognizeResponse)

StreamingRecognitionResult = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESULT,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:StreamingRecognitionResult)
  })
_sym_db.RegisterMessage(StreamingRecognitionResult)

SpeechRecognitionResult = _reflection.GeneratedProtocolMessageType('SpeechRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONRESULT,
  '__module__' : 'stt_pb2'
  # @@protoc_insertion_point(class_scope:SpeechRecognitionResult)
  })
_sym_db.RegisterMessage(SpeechRecognitionResult)



_STT = _descriptor.ServiceDescriptor(
  name='STT',
  full_name='STT',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=575,
  serialized_end=719,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recognize',
    full_name='STT.Recognize',
    index=0,
    containing_service=None,
    input_type=_RECOGNIZEREQUEST,
    output_type=_RECOGNIZERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamingRecognize',
    full_name='STT.StreamingRecognize',
    index=1,
    containing_service=None,
    input_type=_STREAMINGRECOGNIZEREQUEST,
    output_type=_STREAMINGRECOGNIZERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STT)

DESCRIPTOR.services_by_name['STT'] = _STT

# @@protoc_insertion_point(module_scope)
