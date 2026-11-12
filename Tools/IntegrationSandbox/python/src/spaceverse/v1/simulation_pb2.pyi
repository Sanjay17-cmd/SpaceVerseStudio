from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeScale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_SCALE_UNSPECIFIED: _ClassVar[TimeScale]
    TIME_SCALE_SIMULATION_ELAPSED: _ClassVar[TimeScale]
    TIME_SCALE_UTC: _ClassVar[TimeScale]
    TIME_SCALE_TAI: _ClassVar[TimeScale]
    TIME_SCALE_TT: _ClassVar[TimeScale]
    TIME_SCALE_TDB: _ClassVar[TimeScale]

class ReferenceFrame(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REFERENCE_FRAME_UNSPECIFIED: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_ICRF: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_J2000: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_ECEF: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_RTN: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_SPACECRAFT_BODY: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_SENSOR: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_CUSTOM: _ClassVar[ReferenceFrame]

class AxisConvention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AXIS_CONVENTION_UNSPECIFIED: _ClassVar[AxisConvention]
    AXIS_RIGHT_HANDED_Z_UP: _ClassVar[AxisConvention]
    AXIS_RIGHT_HANDED_Y_UP: _ClassVar[AxisConvention]
    AXIS_LEFT_HANDED_Z_UP: _ClassVar[AxisConvention]
    AXIS_CUSTOM: _ClassVar[AxisConvention]

class LengthUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LENGTH_UNIT_UNSPECIFIED: _ClassVar[LengthUnit]
    LENGTH_UNIT_METER: _ClassVar[LengthUnit]
    LENGTH_UNIT_KILOMETER: _ClassVar[LengthUnit]

class VelocityUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VELOCITY_UNIT_UNSPECIFIED: _ClassVar[VelocityUnit]
    VELOCITY_UNIT_METER_PER_SECOND: _ClassVar[VelocityUnit]
    VELOCITY_UNIT_KILOMETER_PER_SECOND: _ClassVar[VelocityUnit]

class AttitudeConvention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ATTITUDE_CONVENTION_UNSPECIFIED: _ClassVar[AttitudeConvention]
    ATTITUDE_BODY_TO_REFERENCE_FRAME_XYZW: _ClassVar[AttitudeConvention]
    ATTITUDE_REFERENCE_FRAME_TO_BODY_XYZW: _ClassVar[AttitudeConvention]
TIME_SCALE_UNSPECIFIED: TimeScale
TIME_SCALE_SIMULATION_ELAPSED: TimeScale
TIME_SCALE_UTC: TimeScale
TIME_SCALE_TAI: TimeScale
TIME_SCALE_TT: TimeScale
TIME_SCALE_TDB: TimeScale
REFERENCE_FRAME_UNSPECIFIED: ReferenceFrame
REFERENCE_FRAME_ICRF: ReferenceFrame
REFERENCE_FRAME_J2000: ReferenceFrame
REFERENCE_FRAME_ECEF: ReferenceFrame
REFERENCE_FRAME_RTN: ReferenceFrame
REFERENCE_FRAME_SPACECRAFT_BODY: ReferenceFrame
REFERENCE_FRAME_SENSOR: ReferenceFrame
REFERENCE_FRAME_CUSTOM: ReferenceFrame
AXIS_CONVENTION_UNSPECIFIED: AxisConvention
AXIS_RIGHT_HANDED_Z_UP: AxisConvention
AXIS_RIGHT_HANDED_Y_UP: AxisConvention
AXIS_LEFT_HANDED_Z_UP: AxisConvention
AXIS_CUSTOM: AxisConvention
LENGTH_UNIT_UNSPECIFIED: LengthUnit
LENGTH_UNIT_METER: LengthUnit
LENGTH_UNIT_KILOMETER: LengthUnit
VELOCITY_UNIT_UNSPECIFIED: VelocityUnit
VELOCITY_UNIT_METER_PER_SECOND: VelocityUnit
VELOCITY_UNIT_KILOMETER_PER_SECOND: VelocityUnit
ATTITUDE_CONVENTION_UNSPECIFIED: AttitudeConvention
ATTITUDE_BODY_TO_REFERENCE_FRAME_XYZW: AttitudeConvention
ATTITUDE_REFERENCE_FRAME_TO_BODY_XYZW: AttitudeConvention

class Vector3d(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Quaterniond(_message.Message):
    __slots__ = ("x", "y", "z", "w")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    w: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., w: _Optional[float] = ...) -> None: ...

class SimulationTime(_message.Message):
    __slots__ = ("elapsed_seconds", "time_scale", "epoch_julian_date")
    ELAPSED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    EPOCH_JULIAN_DATE_FIELD_NUMBER: _ClassVar[int]
    elapsed_seconds: float
    time_scale: TimeScale
    epoch_julian_date: float
    def __init__(self, elapsed_seconds: _Optional[float] = ..., time_scale: _Optional[_Union[TimeScale, str]] = ..., epoch_julian_date: _Optional[float] = ...) -> None: ...

class StreamStateRequest(_message.Message):
    __slots__ = ("run_id", "entity_ids", "max_updates", "interval_ms", "client_name")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    MAX_UPDATES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    entity_ids: _containers.RepeatedScalarFieldContainer[str]
    max_updates: int
    interval_ms: int
    client_name: str
    def __init__(self, run_id: _Optional[str] = ..., entity_ids: _Optional[_Iterable[str]] = ..., max_updates: _Optional[int] = ..., interval_ms: _Optional[int] = ..., client_name: _Optional[str] = ...) -> None: ...

class GetLatestStateRequest(_message.Message):
    __slots__ = ("run_id", "entity_id")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    entity_id: str
    def __init__(self, run_id: _Optional[str] = ..., entity_id: _Optional[str] = ...) -> None: ...

class StateSnapshot(_message.Message):
    __slots__ = ("schema_version", "run_id", "entity_id", "sequence_number", "simulation_time", "position", "velocity", "attitude", "reference_frame", "custom_reference_frame", "axis_convention", "position_unit", "velocity_unit", "attitude_convention", "is_valid", "producer_name", "producer_version")
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ATTITUDE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    AXIS_CONVENTION_FIELD_NUMBER: _ClassVar[int]
    POSITION_UNIT_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_UNIT_FIELD_NUMBER: _ClassVar[int]
    ATTITUDE_CONVENTION_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_VERSION_FIELD_NUMBER: _ClassVar[int]
    schema_version: str
    run_id: str
    entity_id: str
    sequence_number: int
    simulation_time: SimulationTime
    position: Vector3d
    velocity: Vector3d
    attitude: Quaterniond
    reference_frame: ReferenceFrame
    custom_reference_frame: str
    axis_convention: AxisConvention
    position_unit: LengthUnit
    velocity_unit: VelocityUnit
    attitude_convention: AttitudeConvention
    is_valid: bool
    producer_name: str
    producer_version: str
    def __init__(self, schema_version: _Optional[str] = ..., run_id: _Optional[str] = ..., entity_id: _Optional[str] = ..., sequence_number: _Optional[int] = ..., simulation_time: _Optional[_Union[SimulationTime, _Mapping]] = ..., position: _Optional[_Union[Vector3d, _Mapping]] = ..., velocity: _Optional[_Union[Vector3d, _Mapping]] = ..., attitude: _Optional[_Union[Quaterniond, _Mapping]] = ..., reference_frame: _Optional[_Union[ReferenceFrame, str]] = ..., custom_reference_frame: _Optional[str] = ..., axis_convention: _Optional[_Union[AxisConvention, str]] = ..., position_unit: _Optional[_Union[LengthUnit, str]] = ..., velocity_unit: _Optional[_Union[VelocityUnit, str]] = ..., attitude_convention: _Optional[_Union[AttitudeConvention, str]] = ..., is_valid: _Optional[bool] = ..., producer_name: _Optional[str] = ..., producer_version: _Optional[str] = ...) -> None: ...
