"""Deterministic, explicitly non-flight, circular-LEO sample state generator."""
from __future__ import annotations

import math

from spaceverse.v1 import simulation_pb2 as pb

# Earth standard gravitational parameter in km^3/s^2. Used solely to produce
# repeatable synthetic demonstration data; this is not the SpaceVerse flight
# astrodynamics implementation or a validated mission propagator.
EARTH_MU_KM3_S2 = 398600.4418
MOCK_RUN_ID = "spaceverse-local-mock-run-001"
MOCK_SCHEMA_VERSION = "1.0"

# entity_id: (circular radius in km, initial phase in radians)
MOCK_ENTITIES: dict[str, tuple[float, float]] = {
    "terra-001": (7000.0, 0.0),
    "demo-sat-002": (7200.0, math.pi / 2.0),
}

CUSTOM_FRAME_NAME = "SV_TEST_EARTH_CENTRED_INERTIAL_RH_Z_UP"


def circular_state_km(radius_km: float, elapsed_seconds: float, phase0_rad: float = 0.0):
    """Return position km and velocity km/s for a simple circular two-body fixture."""
    if not math.isfinite(radius_km) or radius_km <= 0.0:
        raise ValueError("radius_km must be a positive finite number")
    if not math.isfinite(elapsed_seconds) or elapsed_seconds < 0.0:
        raise ValueError("elapsed_seconds must be finite and non-negative")

    mean_motion_rad_s = math.sqrt(EARTH_MU_KM3_S2 / (radius_km ** 3))
    phase = phase0_rad + mean_motion_rad_s * elapsed_seconds
    cos_phase = math.cos(phase)
    sin_phase = math.sin(phase)

    position = (
        radius_km * cos_phase,
        radius_km * sin_phase,
        0.0,
    )
    velocity = (
        -radius_km * mean_motion_rad_s * sin_phase,
        radius_km * mean_motion_rad_s * cos_phase,
        0.0,
    )
    return position, velocity


def make_snapshot(entity_id: str, sequence_number: int, elapsed_seconds: float, run_id: str = MOCK_RUN_ID):
    """Build one versioned protobuf snapshot for a known mock entity."""
    if entity_id not in MOCK_ENTITIES:
        raise ValueError(f"Unknown mock entity_id: {entity_id}")
    if sequence_number < 0:
        raise ValueError("sequence_number must be non-negative")

    radius_km, phase0_rad = MOCK_ENTITIES[entity_id]
    position, velocity = circular_state_km(radius_km, elapsed_seconds, phase0_rad)

    return pb.StateSnapshot(
        schema_version=MOCK_SCHEMA_VERSION,
        run_id=run_id,
        entity_id=entity_id,
        sequence_number=sequence_number,
        simulation_time=pb.SimulationTime(
            elapsed_seconds=elapsed_seconds,
            time_scale=pb.TIME_SCALE_SIMULATION_ELAPSED,
        ),
        position=pb.Vector3d(x=position[0], y=position[1], z=position[2]),
        velocity=pb.Vector3d(x=velocity[0], y=velocity[1], z=velocity[2]),
        attitude=pb.Quaterniond(x=0.0, y=0.0, z=0.0, w=1.0),
        reference_frame=pb.REFERENCE_FRAME_CUSTOM,
        custom_reference_frame=CUSTOM_FRAME_NAME,
        axis_convention=pb.AXIS_RIGHT_HANDED_Z_UP,
        position_unit=pb.LENGTH_UNIT_KILOMETER,
        velocity_unit=pb.VELOCITY_UNIT_KILOMETER_PER_SECOND,
        attitude_convention=pb.ATTITUDE_BODY_TO_REFERENCE_FRAME_XYZW,
        is_valid=True,
        producer_name="SpaceVerseIntegrationSandbox",
        producer_version="0.1.0",
    )
