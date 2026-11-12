"""Fail-closed structural and numerical validation for incoming snapshots."""
from __future__ import annotations

import math

from spaceverse.v1 import simulation_pb2 as pb


def validate_snapshot(snapshot: pb.StateSnapshot) -> None:
    """Raise ValueError if a snapshot is unsafe/ambiguous for visualization."""
    if snapshot.schema_version != "1.0":
        raise ValueError(f"Unsupported schema_version: {snapshot.schema_version!r}")
    if not snapshot.run_id.strip():
        raise ValueError("run_id is required")
    if not snapshot.entity_id.strip():
        raise ValueError("entity_id is required")
    if not snapshot.HasField("simulation_time"):
        raise ValueError("simulation_time is required")
    if not snapshot.HasField("position") or not snapshot.HasField("velocity"):
        raise ValueError("position and velocity are required")
    if not snapshot.HasField("attitude"):
        raise ValueError("attitude quaternion is required")
    if not snapshot.is_valid:
        raise ValueError("producer marked snapshot as invalid")

    if snapshot.simulation_time.time_scale == pb.TIME_SCALE_UNSPECIFIED:
        raise ValueError("time_scale must be explicit")
    if snapshot.reference_frame == pb.REFERENCE_FRAME_UNSPECIFIED:
        raise ValueError("reference_frame must be explicit")
    if snapshot.reference_frame == pb.REFERENCE_FRAME_CUSTOM and not snapshot.custom_reference_frame.strip():
        raise ValueError("custom_reference_frame is required for CUSTOM frame")
    if snapshot.axis_convention == pb.AXIS_CONVENTION_UNSPECIFIED:
        raise ValueError("axis_convention must be explicit")
    if snapshot.position_unit == pb.LENGTH_UNIT_UNSPECIFIED:
        raise ValueError("position_unit must be explicit")
    if snapshot.velocity_unit == pb.VELOCITY_UNIT_UNSPECIFIED:
        raise ValueError("velocity_unit must be explicit")
    if snapshot.attitude_convention == pb.ATTITUDE_CONVENTION_UNSPECIFIED:
        raise ValueError("attitude_convention must be explicit")

    numeric_values = (
        snapshot.simulation_time.elapsed_seconds,
        snapshot.position.x, snapshot.position.y, snapshot.position.z,
        snapshot.velocity.x, snapshot.velocity.y, snapshot.velocity.z,
        snapshot.attitude.x, snapshot.attitude.y, snapshot.attitude.z, snapshot.attitude.w,
    )
    if not all(math.isfinite(value) for value in numeric_values):
        raise ValueError("snapshot contains a non-finite numeric value")
    if snapshot.simulation_time.elapsed_seconds < 0.0:
        raise ValueError("elapsed_seconds must be non-negative")
    if snapshot.simulation_time.HasField("epoch_julian_date"):
        if not math.isfinite(snapshot.simulation_time.epoch_julian_date):
            raise ValueError("epoch_julian_date must be finite when present")
        if snapshot.simulation_time.time_scale == pb.TIME_SCALE_UNSPECIFIED:
            raise ValueError("time_scale must be explicit when epoch_julian_date is present")

    q = snapshot.attitude
    norm = math.sqrt(q.x*q.x + q.y*q.y + q.z*q.z + q.w*q.w)
    if not math.isclose(norm, 1.0, rel_tol=0.0, abs_tol=1e-6):
        raise ValueError(f"attitude quaternion must be normalized; norm={norm}")
