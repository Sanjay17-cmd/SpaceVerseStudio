# Unreal integration plan (not yet compiled into the project)

## Current boundary

The Python mock server and its CLI client validate the protobuf contract independently. They do not yet connect to Unreal. This is intentional: the Unreal C++ gRPC transport dependency and runtime team's final contract must be agreed before introducing generated C++ stubs or a third-party plugin into the UE 5.8 build.

## Planned Unreal-side files

When the transport is approved, keep the Unreal adapter in this same codebase/repository under the project module, for example:

- `Source/SpaceVerseStudio/Integration/SVTelemetryClient.h/.cpp`
- `Source/SpaceVerseStudio/Integration/SVTelemetrySubsystem.h/.cpp`
- `Source/SpaceVerseStudio/Integration/SVCoordinateAdapter.h/.cpp`
- `Source/SpaceVerseStudio/Integration/SVSnapshotValidator.h/.cpp`
- generated C++ protobuf/gRPC files under a dedicated generated-code directory (do not hand-edit)
- automated tests under `Source/SpaceVerseStudio/Tests/` or the project's agreed test module

## Required runtime-team decisions before coordinate conversion

- authoritative reference frame and frame realization;
- axis directions and handedness;
- position and velocity units;
- quaternion component order and rotation direction;
- simulation epoch and time scale;
- entity ID lifecycle and uniqueness scope;
- sequence-number semantics and snapshot cadence;
- whether snapshots are full states or deltas;
- reconnect, timeout, cancellation, and backpressure behavior.

## Rendering rule

The runtime remains authoritative. Unreal consumes immutable snapshots and may interpolate render poses between snapshots. Render interpolation must never be fed back into physical simulation. The mock contract uses an explicitly named custom test frame and must not be interpreted as a flight/reference frame.
